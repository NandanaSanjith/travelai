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
      <search-bar />
      <flight-list-view
        start-date="2025-10-01"
        end-date="2025-10-02"
      />
      
    </v-main>
    
    
    
  </v-app>
</template>

<script setup>
import SearchBar from './components/SearchBar.vue';
import FlightListView from './components/FlightListView.vue';
</script>