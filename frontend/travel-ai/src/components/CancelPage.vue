<template>
 <div>
    <h1>Booking Failed</h1>
    <p>Booking ID: {{ bookingId }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const bookingId=route.query.booking_id
</script>