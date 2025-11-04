<template>
  <!-- Chat toggle button -->
  <v-btn
    color="primary"
    fab
    fixed
    bottom
    right
    size="x-large"
    elevation="6"
    class="chat-button ma-4"
    icon="mdi-chat"
    @click="toggleChat"
  />

  <!-- Chat window -->
  <v-slide-y-transition>
    <v-card
      v-if="isOpen"
      class="chat-window"
      elevation="8"
      min-height="500"
    >
      <!-- Header -->
      <v-card-title class="d-flex justify-space-between align-center">
        <div class="d-flex align-center">
          <v-icon class="mr-2" color="red">mdi-creation</v-icon>
          <span>Support Chat</span>
        </div>
        <div>
          <v-btn icon @click="clearChat" title="Clear Chat" class="mr-1">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
          <v-btn icon @click="toggleChat" title="Close Chat">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </div>
      </v-card-title>

      <!-- Messages -->
      <v-card-text class="chat-messages">
        <div ref="messagesContainer" class="messages-container">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            :class="['message', msg.from]"
            :style="{
              'text-align': msg.from === 'bot' ? 'left' : 'right',
              'margin-left': msg.from === 'user' ? 'auto' : '0',
              'margin-right': msg.from === 'bot' ? 'auto' : '0'
            }"
          >
            <div v-if="msg.from === 'bot'" v-html="renderMarkdown(msg.text)"></div>
            <div v-else>{{ msg.text }}</div>
          </div>
        </div>
      </v-card-text>

      <!-- Input -->
      <v-card-actions class="chat-input">
        <v-textarea
          v-model="newMessage"
          placeholder="Type a message..."
          hide-details
          no-resize
          rounded
          variant="outlined"
          rows="2"
          :disabled="isLoading"
          @keyup.enter="sendMessage"
        />
        <v-btn color="primary" :loading="isLoading" :disabled="isLoading" @click="sendMessage">Send</v-btn>
      </v-card-actions>
    </v-card>
  </v-slide-y-transition>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
})

const isOpen = ref(false)
const messages = ref([
  { from: 'bot', text: 'Hello! How can I help you?' }
])
const newMessage = ref('')
const isLoading =ref(false)
const resetConversation = ref(true)
const messagesContainer = ref(null)

watch(messages, async () => {
  await nextTick()
  scrollToBottom()
}, { deep: true })

function scrollToBottom() {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

function renderMarkdown(text) {
  return md.render(text || '')
}

// Add target="_blank" to all links
const defaultRender = md.renderer.rules.link_open || function(tokens, idx, options, env, self) {
  return self.renderToken(tokens, idx, options);
};

md.renderer.rules.link_open = function (tokens, idx, options, env, self) {
  const aIndex = tokens[idx].attrIndex('target');

  if (aIndex < 0) {
    tokens[idx].attrPush(['target', '_blank']);
  } else {
    tokens[idx].attrs[aIndex][1] = '_blank';
  }

  return defaultRender(tokens, idx, options, env, self);
};

function toggleChat() {
  isOpen.value = !isOpen.value
}

function clearChat() {
  messages.value = [{ from: 'bot', text: 'Hello! How can I help you?' }]
  resetConversation.value = true
}

async function sendMessage() {
  if (!newMessage.value.trim()) return
  isLoading.value=true

  const messageText = newMessage.value
  messages.value.push({ from: 'user', text: messageText })
  newMessage.value = ''

  try {
    const response = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: messageText, reset_conversation: resetConversation.value })
    })

    if (!response.ok) {
      throw new Error('Failed to get response from server')
    }
    const data = await response.json()
    messages.value.push({ from: 'bot', text: data.response })
    resetConversation.value = false
    console.log(data.response)

  } catch (error) {
    console.error('Chat error:', error)
    messages.value.push({
      from: 'bot',
      text: 'Sorry, I encountered an error. Please try again later.'
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.message :deep(a) {
  color: #1976d2;
  text-decoration: none;
}

.message :deep(a:hover) {
  text-decoration: underline;
}

.message :deep(code) {
  background: #f5f5f5;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: monospace;
}

.message :deep(pre) {
  background: #f5f5f5;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
  margin: 8px 0;
}

.message :deep(ul),
.message :deep(ol) {
  margin: 8px 0;
  padding-left: 24px;
}

.message :deep(blockquote) {
  border-left: 3px solid #ddd;
  margin: 8px 0;
  padding-left: 12px;
  color: #666;
}

.chat-window {
  position: fixed;
  bottom: 100px; /* above the fab button */
  right: 60px;
  width: 380px;
  max-height: 500px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 1000;
}

/* Messages styling */
.chat-messages {
  flex: 1;
  max-height: 650px;
  overflow-y: auto;
  padding: 10px;
  background-color: #f5f5f5;
}

/* Message bubbles */
.message {
  padding: 8px 12px;
  margin: 6px 0;
  border-radius: 12px;
  max-width: 80%;
}
.message.user {
  background-color: #1976d2;
  color: white;
  align-self: flex-end;
}

/* Input styling */
.chat-input {
  display: flex;
  gap: 8px;
  padding: 8px;
}

.chat-button {
  z-index: 1000; /* Ensures it stays above other elements */
  position: fixed;
  bottom: 20px;
  right: 20px;
  transition: transform 0.2s ease-in-out;
}

.chat-button:hover {
  transform: scale(1.1); /* Slight scale effect on hover */
}

.messages-container {
  height: 100%;
  overflow-y: auto;
  padding-right: 8px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
</style>

