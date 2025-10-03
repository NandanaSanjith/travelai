<template>
 <v-list lines="one">
  <v-card 
    v-for="flight in flightDetails"
    :key="flight.id"
    elevation="16"
    class="ma-2 pa-4"
   >
   <v-list-item >
       {{ flight.airline}}
       {{ flight.departure_date }}
       {{ flight.departure_city }}
       {{ flight.arrival_city }}
       {{ flight.price }}
       {{ flight.available_seats }}
    </v-list-item>
   </v-card> 
 </v-list>
</template>

<script setup>
import { ref, onMounted } from 'vue';


const flightDetails = ref([]);

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
defineExpose({ onSearchChanged })
</script>

<style>
</style>