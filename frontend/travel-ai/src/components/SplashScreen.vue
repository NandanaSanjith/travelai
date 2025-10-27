<template>
  <div class="splash-screen">
    <img src="../assets/wanderwise-icon.svg" alt="App Logo" class="logo" />
    <h1 class="app-name">WanderWise</h1>
  </div>
</template>

<script setup>
// No logic yet — it's a static splash
</script>

<style scoped>
.splash-screen {
  position: fixed;
  inset: 0;
  background-color: #121212;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  transition: opacity 0.6s ease;
}

.logo {
  width: 100px;
  animation: pulse 1.5s infinite ease-in-out;
}

@keyframes pulse {
  0%, 100% { opacity: 0.7; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.1); }
}
</style>
