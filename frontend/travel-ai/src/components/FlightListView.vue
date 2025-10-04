<template>
 
  <v-card 
    v-for="flight in flightDetails"
    :key="flight.id"
    elevation="2"
    class="my-2 py-4"
   >
   
       {{ flight.airline}}
       {{ flight.departure_date }}
       {{ flight.departure_city }}
       {{ flight.arrival_city }}
       {{ flight.price }}
       {{ flight.available_seats }}
       <v-btn color="primary" @click="onClickEvent">Book</v-btn>
    
   </v-card> 
</template>

<script setup>
import { ref, defineEmits } from 'vue';
const flightDetails = ref([]);
const emit = defineEmits(['showBookingView'])

const fetchFlightDetails = async (sourceCity,destCity,startDate) => { 
  const url = `http://127.0.0.1:8000/flights?src_city=${sourceCity}&dest_city=${destCity}&start_date=${startDate}`

  const response = await fetch(url); 
  if (!response.ok) {
      console.error("failed to fetch data")
    }
    flightDetails.value = await response.json();
}

const onSearchChanged = async(sourceCity,destCity,startDate) => {
  fetchFlightDetails(sourceCity,destCity,startDate);
};
const onClickEvent = async() => {
  emit('showBookingView')
};

defineExpose({ onSearchChanged })
</script>

<style>
</style>