<template>
 <v-list lines="one">
  <v-list-item
    v-for="flight in flightDetails"
    :key="flight.id"
   >
   {{ flight.airline }}
  </v-list-item>
 </v-list>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const flightDetails = ref([]);

const fetchFlightDetails = async () => { 
  const response = await fetch('http://127.0.0.1:8000/flights?src_city=kochi&dest_city=bangalore&start_date=2025-09-30'); 
  if (!response.ok) {
      console.error("failed to fetch data")
    }
    flightDetails.value = await response.json();
}

onMounted(() => {
  fetchFlightDetails();
});

</script>

<style>
</style>