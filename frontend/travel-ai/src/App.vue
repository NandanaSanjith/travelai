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
      <div
       v-if="!canShowBookingView"
      >
       <search-bar
        :airports="airports"
        @on-search="onSearchEvent"/>
        
       <flight-list-view
         ref="flightListView"
         class="mt-4"
         @show-booking-view="onShowBookingView"
        />
      </div>

      <booking-view 
        v-if="canShowBookingView"
      >
      </booking-view>
    </v-main>
    
    
    
  </v-app>
</template>

<script setup>
import { ref,onMounted} from "vue"
import SearchBar from './components/SearchBar.vue';
import FlightListView from './components/FlightListView.vue';
import BookingView from "./components/BookingView.vue";
const flightListView=ref(null)
const canShowBookingView=ref(false)
const airports=ref([])

const onSearchEvent = (query) => {
  flightListView.value.onSearchChanged(query.sourceCity,query.destCity,query.date)
}
const onShowBookingView = () => {
  canShowBookingView.value=true
}


const fetchAirports = async () => {
  try {
    const url = 'http://127.0.0.1:8000/airports';
    const response = await fetch(url);
    if (!response.ok) throw new Error('Failed to fetch airpots');
    airports.value = await response.json();
    console.log(airports.value)
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
  fetchAirports()
})
</script>