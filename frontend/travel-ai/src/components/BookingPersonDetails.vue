<template>
 <div>
  <!-- Name -->
  <v-text-field 
   label="Name"
   v-model="localName"
   @input="emit('update:name', localName)"
  >
  </v-text-field>

  <!-- Email with validation -->
  <v-text-field 
   label="Email"
   v-model="localEmail"
   :error="!isEmailValid && localEmail.length > 0"
   :error-messages="emailError"
   @input="handleEmailInput"
  >
  </v-text-field>
 </div>
</template>

<script setup>
import { ref, defineEmits, defineProps, computed } from 'vue'

const emit = defineEmits(['update:name', 'update:email'])

defineProps({
  name: String,
  email: String
})

const localName = ref('')
const localEmail = ref('')

// ✅ Email validation regex
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

// ✅ Computed properties for validation state
const isEmailValid = computed(() => emailPattern.test(localEmail.value))
const emailError = computed(() => {
  if (localEmail.value === '') return ''
  return isEmailValid.value ? '' : 'Please enter a valid email address'
})

// ✅ Emit only when user types
const handleEmailInput = () => {
  emit('update:email', localEmail.value)
}
</script>

<style>
</style>
