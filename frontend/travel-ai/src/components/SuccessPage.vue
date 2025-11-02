<template>
 <div>
    <v-avatar
     color="success"
     size="100"
     class="mb-4"
    >
      <v-icon size="60" color="white">mdi-check-circle</v-icon>
    </v-avatar>


    <!-- Success Message -->
    <h1 class="text-h3 font-weight-bold text-success mb-4">
    Booking Successful!
    </h1>


    <v-divider class="my-4"></v-divider>


    <!-- Booking ID -->
    <v-card
     v-if="bookingData"
     color="grey-lighten-4"
     flat
     rounded="lg"
     class="pa-4 mb-6"
    >
        <div class="text-overline text-grey-darken-1 mb-2">
          Your Booking ID
        </div>
        <div class="text-h5 font-weight-bold text-primary">
          {{ bookingData.booking_details.booking_id }}
        </div>
    </v-card>

    <manage-booking-view
      v-if="bookingData"
      :booking-data="bookingData"
    />
    <weather-widget
      v-if="bookingData"
      :city="bookingData.flight_details.arrival_city"
      class="mt-6"
    />
  </div>
</template>

<script setup>
import {ref,onMounted} from 'vue' ;
import { useRoute } from 'vue-router';
import ManageBookingView from './ManageBookingView.vue';
const route = useRoute();
const bookingId=route.query.booking_id
const bookingData=ref(null)
import WeatherWidget from './WeatherWidget.vue';
const fetchBookingDetails = async () => {
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
 if (bookingId) {
   fetchBookingDetails();
 } else {
   loading.value = false;
 }
});




</script>