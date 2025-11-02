<template>
 <div>
    <h1>Booking Successful</h1>
    <p>Booking ID: {{ bookingId }}</p>
    <manage-booking-view
      v-if="bookingData"
      :booking-data="bookingData"
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