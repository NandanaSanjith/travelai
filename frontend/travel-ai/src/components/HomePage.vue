<template>
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
        :flight="selectedFlight"
        class="mx-auto"
        style="width:720px"
      >
      </booking-view>
      
</template>
<script setup>
import { ref,onMounted} from "vue"
import SearchBar from './SearchBar.vue';
import FlightListView from './FlightListView.vue';
import BookingView from "./BookingView.vue";
const flightListView=ref(null)
const canShowBookingView=ref(false)
const airports=ref([])
const selectedFlight=ref(null)

const onSearchEvent = (query) => {
  flightListView.value.onSearchChanged(query.sourceCity,query.destCity,query.date)
}
const onShowBookingView = (flight) => {
  selectedFlight.value = flight
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