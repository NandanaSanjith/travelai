<template>
 <v-card
   class="mx-auto mt-8"
   max-width="900"
   color="blue-lighten-4"
   elevation="8"
   rounded="xl"
 >
   <v-card-text class="text-center">
     <!-- City Title -->
     <h2 class="text-h5 font-weight-bold mb-4">{{ city.toUpperCase() }}</h2>


     <!-- Current weather -->
     <div v-if="current">
       <v-img
         :src="`https://openweathermap.org/img/wn/${current.weather[0].icon}@2x.png`"
         alt="weather icon"
         width="80"
         height="80"
         class="mx-auto"
       />
       <div class="text-h2 font-weight-bold my-2">
         {{ current.main.temp.toFixed(1) }}°C
       </div>
       <div class="text-subtitle-1 text-capitalize">
         {{ current.weather[0].description }}
       </div>
     </div>


     <!-- Forecast -->
     <v-row v-if="forecast.length" class="mt-6 d-flex justify-space-between" no-gutters>
       <v-col
         v-for="(day, i) in forecast"
         :key="i"
         cols="auto"
         class="mx-1"
       >
         <v-card
           class="pa-3 text-center"
           color="white"
           elevation="2"
           rounded="lg"
           min-width="90"
         >
           <div class="font-weight-bold text-body-2 mb-2">
             {{ formatDay(day.dt_txt) }}
           </div>
           <v-img
             :src="`https://openweathermap.org/img/wn/${day.weather[0].icon}.png`"
             alt="icon"
             width="40"
             height="40"
             class="mx-auto"
           />
           <div class="text-caption mt-2">
             {{ Math.round(day.main.temp_max) }}° / {{ Math.round(day.main.temp_min) }}°
           </div>
         </v-card>
       </v-col>
     </v-row>


     <!-- Loading state -->
     <v-progress-circular
       v-if="!current"
       indeterminate
       color="primary"
       class="mt-4"
     />
   </v-card-text>
 </v-card>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'


// Props
const props = defineProps({
 city: { type: String, required: true },
})


const current = ref(null)
const forecast = ref([])


async function fetchWeather() {
 try {
   const apiKey = import.meta.env.VITE_WEATHER_API_KEY
   console.log(apiKey)
   // Fetch current weather
   const currentRes = await axios.get('https://api.openweathermap.org/data/2.5/weather', {
     params: {
       q: props.city,
       units: 'metric',
       appid: apiKey
     }
   })
   current.value = currentRes.data


   // Fetch 5-day forecast (every 3 hours)
   const forecastRes = await axios.get('https://api.openweathermap.org/data/2.5/forecast', {
     params: {
       q: props.city,
       units: 'metric',
       appid: apiKey
     }
   })


   // Filter forecast → one entry per day (midday)
   const daily = forecastRes.data.list.filter(item => item.dt_txt.includes('12:00:00'))
   forecast.value = daily.slice(0, 5)
 } catch (error) {
   console.error('Weather fetch failed:', error)
 }
}


function formatDay(dateStr) {
 const date = new Date(dateStr)
 return date.toLocaleDateString('en-US', { weekday: 'short' })
}


onMounted(fetchWeather)
watch(() => props.city, fetchWeather)
</script>



