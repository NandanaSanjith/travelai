<template> 
  <v-card elevation="8" class="pa-4 d-flex align-center" style="border-radius: 14px;">
      <v-select
        v-model="travelType"
        :items="['Flight', 'Train', 'Bus']"
        label="Mode"
        variant="outlined"
        class="mx-2"
        style="max-width: 150px;"
      />

      <v-text-field v-model="from" label="From" variant="outlined" class="mx-2 flex-grow-1" />
      <v-text-field v-model="to" label="To" variant="outlined" class="mx-2 flex-grow-1" />
      <v-text-field v-model="date" type="date" label="Date" variant="outlined" class="mx-2" style="max-width: 200px;" />

      <v-btn color="primary" class="ml-3 px-6" height="56" @click="handleSearch">
        🔍 Search
      </v-btn>
  </v-card>

    <!-- Dynamic Sections -->
    <v-container class="mt-6">
      <!-- Flight Booking -->
      <div v-if="section === 'Flight'">
        <v-alert type="success" border="start" class="mb-4">✈️ Flight Booking Section</v-alert>
        <p>Here you can show flight search results, filters, and booking details.</p>
      </div>

      <!-- Train Booking -->
      <div v-if="section === 'Train'">
        <v-alert type="info" border="start" class="mb-4">🚆 Train Booking Section</v-alert>
        <p>Here you can display train schedules, seats, and booking options.</p>
      </div>

      <!-- Bus Booking -->
      <div v-if="section === 'Bus'">
        <v-alert type="warning" border="start" class="mb-4">🚌 Bus Booking Section</v-alert>
        <p>Here you can display bus operators, timings, and booking choices.</p>
      </div>
    </v-container>
</template>

<script setup>
import { ref } from "vue"

const travelType = ref("Flight")
const from = ref("")
const to = ref("")
const date = ref("")

const section = ref(null)

const handleSearch = () => {
  section.value = travelType.value // switch to chosen section
}
</script>

<style>
</style>