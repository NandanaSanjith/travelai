<template>
   <div class="background-container">
     <v-card
       elevation="10"
       class="search-card d-flex flex-wrap align-center justify-center"
       style="border-radius: 0px; background-color: rgba(255, 255, 255, 1); width: 100%;"
     >
       <!-- Booking ID Input -->
       <v-text-field
         v-model="bookingId"
         label="Enter Booking ID"
         variant="outlined"
         style="flex: 1; max-width: 400px;"
         hide-details
         rounded
         prepend-inner-icon="mdi-ticket-confirmation"
         clearable
       />


       <!-- Show Booking Details Button -->
       <v-btn
         color="primary"
         height="56"
         @click="handleShowBookingDetails"
         prepend-icon="mdi-magnify"
         elevation="4"
         class="mx-2"
         :disabled="!bookingId"
       >
         Show Details
       </v-btn>


       <!-- Switch to Search Button -->
       <v-btn
         color="secondary"
         height="56"
         variant="outlined"
         @click="handleSwitchToSearch"
         prepend-icon="mdi-airplane-search"
         elevation="2"
       >
         Search Flights
       </v-btn>
     </v-card>
   </div>
</template>


<script setup>
import { ref } from "vue"


const emit = defineEmits(['onGetBookingDetails', 'onSwitchToSearch'])


const bookingId = ref('')


const handleShowBookingDetails = () => {
 if (bookingId.value) {
   emit('onGetBookingDetails', bookingId.value)
 }
}


const handleSwitchToSearch = () => {
 emit('onSwitchToSearch')
}
</script>


<style scoped>
/* 🌇 Background Image */
.background-container {
 background-image: url('https://i.pinimg.com/1200x/94/3c/ce/943cce9a94bc0296b52bf5a3360d6125.jpg');
 background-size: cover;
 background-position: center;
 min-height: 320px;
 min-width: 1024px;
 display: flex;
 align-items: flex-end;
 justify-content: center;
}


/* Card */
.search-card {
 gap: 12px;
 padding: 18px;
 box-shadow: 0 8px 24px rgba(20, 30, 60, 0.12);
 transition: all 0.25s ease;
}
</style>

