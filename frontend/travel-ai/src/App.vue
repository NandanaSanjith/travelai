<template>
  <v-app >
    <v-app-bar :elevation="2">
      <v-btn 
          height="120"
          width="160"
          class="d-flex align-center justify-center" 
          @click="goToHome"
        >
          <v-img
            src="src/assets/wanderwise-icon.svg"
            height="120"
            width="160"
          />
        </v-btn>
    </v-app-bar>
    
    <v-main>
      <SplashScreen v-if="loading" />
    <router-view v-else />
    </v-main>
    
    
    
  </v-app>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import SplashScreen from './components/SplashScreen.vue'

const loading = ref(true)

const router = useRouter();
const goToHome = () => {
  router.push('/');
};
onMounted(() => {
  // Simulate app loading or API call delay
  setTimeout(() => {
    loading.value = false
  }, 3000) // 2 seconds splash duration
})
</script>