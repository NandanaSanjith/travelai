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
      <search-bar @on-search="onSearchEvent"/>
      <flight-list-view
        ref="flightListView"
        class="mt-4"
      />
      
    </v-main>
    
    
    
  </v-app>
</template>

<script setup>
import { ref} from "vue"
import SearchBar from './components/SearchBar.vue';
import FlightListView from './components/FlightListView.vue';
const flightListView=ref(null)

const onSearchEvent = (query) => {
  flightListView.value.onSearchChanged(query.sourceCity,query.destCity,query.date)
}
</script>