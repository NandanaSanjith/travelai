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
       {{ startDate }}
       {{ endDate }}
    </v-list-item>
   </v-card> 
 </v-list>
</template>

<script setup>
import { ref, onMounted } from 'vue';

defineProps({
  startDate: String,
  endDate:String
})

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