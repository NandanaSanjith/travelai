<template>
    <div
       v-if="!canShowBookingView"
      >
       <search-bar
        :airports="airports"
        :is-loading="isLoading"
        @on-search="onSearchEvent"/>

        <div class="mt-4">
            <v-skeleton-loader v-if="isLoading" type="card"></v-skeleton-loader>
            <flight-list-view
            v-else
            ref="flightListView"
            class="mt-4"
            :flight-list="flightDetails"
            @show-booking-view="onShowBookingView"
            />
        </div>
        
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
const isLoading=ref(false)
const flightDetails = ref([]);

const onSearchEvent = async (query) => {
    isLoading.value=true
    await fetchFlightDetails(query.sourceCity,query.destCity,query.date)
    isLoading.value=false
}
const onShowBookingView = (flight) => {
  selectedFlight.value = flight
  canShowBookingView.value=true
}
const fetchFlightDetails = async (sourceCity, destCity, startDate) => {
  try {
    const url = `http://127.0.0.1:8000/flights?src_city=${sourceCity}&dest_city=${destCity}&start_date=${startDate}`;
    const response = await fetch(url);
    if (!response.ok) throw new Error('Failed to fetch flight data');
    flightDetails.value = await response.json();
  } catch (err) {
    console.error(err.message);
  }
};


const fetchAirports = async () => {
  try {
    const url = 'http://127.0.0.1:8000/airports';
    const response = await fetch(url);
    if (!response.ok) throw new Error('Failed to fetch airpots');
    airports.value = await response.json();
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
  fetchAirports()
})
</script>