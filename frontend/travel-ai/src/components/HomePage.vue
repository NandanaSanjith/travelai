<template>
    <div
     v-if="!canShowBookingView"
    >
      <search-bar
        v-if="!showManageBookingBar"
        :airports="airports"
        :is-loading="isLoading"
        @on-search="onSearchEvent"
        @on-show-manage-booking="onShowManageBookingView"
      />
      <manage-booking-bar
        v-if="showManageBookingBar"
        :airports="airports"
        :is-loading="isLoading"
        @on-get-booking-details="onGetBookingDetails"
        @on-switch-to-search="onSwitchToSearch"
      />
      <div class="mt-4">
        <div v-if="!showBookingDetails">
            <v-skeleton-loader
              v-if="isLoading"
              type="card"
            />
            <flight-list-view
              v-else
              ref="flightListView"
              class="mt-4"
              :flight-list="flightDetails"
              @show-booking-view="onShowBookingView"
            />
        </div>


        <manage-booking-view
          v-if="bookingData && showBookingDetails"
          :booking-data="bookingData"
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
      <chat-widget>
      </chat-widget>
      
</template>
<script setup>
import { ref,onMounted} from "vue"
import SearchBar from './SearchBar.vue';
import FlightListView from './FlightListView.vue';
import BookingView from "./BookingView.vue";
import ChatWidget from "./ChatWidget.vue";
import ManageBookingBar from "./ManageBookingBar.vue";
import ManageBookingView from "./ManageBookingView.vue";
const showManageBookingBar=ref(false)
const showBookingDetails=ref(false)
const flightListView=ref(null)
const canShowBookingView=ref(false)
const airports=ref([])
const selectedFlight=ref(null)
const isLoading=ref(false)
const flightDetails = ref([]);
const bookingData=ref(null)
const loading = ref(true);
const adults = ref(null);

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

const onGetBookingDetails = (bookingId) => {
   fetchBookingDetails(bookingId)
}


const onSwitchToSearch = () => {
 showManageBookingBar.value = false
 showBookingDetails.value = false
}


const onShowManageBookingView = () => {
 bookingData.value = null
 showManageBookingBar.value = true
 showBookingDetails.value = true
}


const fetchBookingDetails = async (bookingId) => {
 try {
   const response = await fetch(`http://127.0.0.1:8000/booking?booking_id=${bookingId}`);
   if (!response.ok) throw new Error('Failed to fetch booking details');
   bookingData.value = await response.json();
   console.log('Booking data:', bookingData.value);
 } catch (error) {
   console.error('Error fetching booking details:', error);
 } finally {
   loading.value = false;
 }
};




onMounted(() => {
  fetchAirports()
})
</script>