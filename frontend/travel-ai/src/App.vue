<template>
  <v-app >
    <v-app-bar :elevation="2">
      <v-btn 
          height="120"
          width="160"
          class="d-flex align-center justify-center" 
        >
          <v-img
            src="src/assets/wanderwise-icon.svg"
            height="120"
            width="160"
          />
        </v-btn>
    </v-app-bar>
    
    <v-main>
      <router-view />
    </v-main>
    
    
    
  </v-app>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
</script>