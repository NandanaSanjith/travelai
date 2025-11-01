<template>
  <div class="background-container">
    <div class="overlay">
      <v-card
        elevation="10"
        class="search-card d-flex flex-wrap align-center"
        style="border-radius: 16px;"
      >
        <!-- Mode -->
        <v-select
          v-model="travelType"
          :items="['Flight', 'Train', 'Bus']"
          label="Mode"
          variant="outlined"
          class="field mode-field"
          density="comfortable"
          hide-details
          rounded
          prepend-inner-icon="mdi-airplane"
        />

        <!-- From -->
        <v-autocomplete
          v-model="sourceCity"
          :items="props.airports"
          :custom-filter="customFilter"
          item-title="name"
          item-value="iata_code"
          clearable
          label="From"
          variant="outlined"
          class="field flex-grow-1"
          style="min-width: 240px;"
          hide-details
          rounded
          prepend-inner-icon="mdi-map-marker"
        >
          <template #item="{ props: itemProps, item }">
            <v-list-item v-bind="itemProps" :title="null" :subtitle="null">
              <v-list-item-title class="item-title">{{ item.raw.name }}</v-list-item-title>
              <v-list-item-subtitle class="item-sub">
                {{ item.raw.municipality }} • {{ item.raw.iata_code }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>
          <template #selection="{ item }">
            {{ item.raw.municipality }} ({{ item.raw.iata_code }})
          </template>
        </v-autocomplete>

        <!-- To -->
        <v-autocomplete
          v-model="destCity"
          :items="props.airports"
          :custom-filter="customFilter"
          item-title="name"
          item-value="iata_code"
          clearable
          label="To"
          variant="outlined"
          class="field flex-grow-1"
          style="min-width: 240px;"
          hide-details
          rounded
          prepend-inner-icon="mdi-map-marker-radius"
        >
          <template #item="{ props: itemProps, item }">
            <v-list-item v-bind="itemProps" :title="null" :subtitle="null">
              <v-list-item-title class="item-title">{{ item.raw.name }}</v-list-item-title>
              <v-list-item-subtitle class="item-sub">
                {{ item.raw.municipality }} • {{ item.raw.iata_code }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>
          <template #selection="{ item }">
            {{ item.raw.municipality }} ({{ item.raw.iata_code }})
          </template>
        </v-autocomplete>

        <!-- Passengers -->
        <div
          class="passenger-box field d-flex align-center"
          @click.stop
          style="min-width: 170px;"
        >
          <div class="passenger-label">Passengers</div>

          <v-btn
            icon
            small
            :disabled="passengers <= minPassengers"
            @click.stop="decrementPassengers"
            class="passenger-btn"
            aria-label="Decrease passengers"
          >
            <v-icon>mdi-minus</v-icon>
          </v-btn>

          <v-text-field
            v-model="passengers"
            type="number"
            class="passenger-input"
            dense
            readonly
            aria-label="Number of passengers"
            hide-details
          />

          <v-btn
            icon
            small
            :disabled="passengers >= maxPassengers"
            @click.stop="incrementPassengers"
            class="passenger-btn"
            aria-label="Increase passengers"
          >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>

        <!-- Date -->
        <v-text-field
          v-model="date"
          type="date"
          label="Date"
          :min="today"
          variant="outlined"
          class="field date-field"
          hide-details
          rounded
          prepend-inner-icon="mdi-calendar"
          style="width: 200px;"
        />

        <!-- Search -->
        <v-btn
          color="primary"
          class="search-btn"
          height="56"
          :loading="props.isLoading"
          @click="handleSearch"
          prepend-icon="mdi-magnify"
          elevation="4"
        >
          Search
        </v-btn>
      </v-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const emit = defineEmits(['onSearch'])

const travelType = ref("Flight")
const sourceCity = ref(null)
const destCity = ref(null)
const date = ref("")
const passengers = ref(1)

const minPassengers = 1
const maxPassengers = 9
const today = new Date().toISOString().split("T")[0]

const props = defineProps({
  airports: {
    type: Array,
    default: () => []
  },
  isLoading: {
    type: Boolean,
    default: false
  }
})

const incrementPassengers = () => {
  if (passengers.value < maxPassengers) passengers.value++
}
const decrementPassengers = () => {
  if (passengers.value > minPassengers) passengers.value--
}

const handleSearch = () => {
  const query = {
    travelType: travelType.value,
    sourceCity: sourceCity.value,
    destCity: destCity.value,
    date: date.value,
    passengers: passengers.value
  }
  emit('onSearch', query)
}

const customFilter = (value, query, item) => {
  const searchText = (query || "").toLowerCase()
  const raw = item.raw || item
  const name = (raw.name || "").toLowerCase()
  const iataCode = (raw.iata_code || "").toLowerCase()
  const municipality = (raw.municipality || "").toLowerCase()

  return name.includes(searchText) ||
         iataCode.includes(searchText) ||
         municipality.includes(searchText)
}
</script>

<style scoped>
/* 🌇 Background Image */
.background-container {
  background-image: url('https://i.pinimg.com/1200x/94/3c/ce/943cce9a94bc0296b52bf5a3360d6125.jpg');
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Light overlay (no blur) */
.overlay {
  background-color: rgba(255, 255, 255, 0);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Card */
.search-card {
  gap: 12px;
  padding: 18px;
  margin: 24px auto;
  max-width: 1200px;
  box-shadow: 0 8px 24px rgba(20, 30, 60, 0.12);
  background: #ffffff;
  border-radius: 16px;
  transition: all 0.25s ease;
}
.search-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.18);
}

/* Fields */
.field {
  min-height: 56px;
  display: flex;
  align-items: center;
}
.mode-field { width: 140px; }

.item-title { font-weight: 600; font-size: 0.95rem; }
.item-sub { font-size: 0.82rem; color: #6b7280; }

/* Passengers */
.passenger-box {
  border-radius: 10px;
  padding: 6px 10px;
  background: #f9fafb;
  border: 1px solid rgba(16, 24, 40, 0.08);
}
.passenger-label {
  font-size: 0.85rem;
  color: rgba(0, 0, 0, 0.65);
  margin-right: 8px;
}
.passenger-btn {
  min-width: 36px;
  width: 36px;
  height: 36px;
  margin: 0 4px;
  color: #1f2937;
  transition: transform 0.12s ease;
}
.passenger-btn:active { transform: scale(0.95); }

.passenger-input { width: 56px; }
.passenger-input .v-field__outline, 
.passenger-input .v-field__background {
  border: none;
  background: transparent;
}
.passenger-input input[readonly] {
  text-align: center;
  font-weight: 700;
  font-size: 0.98rem;
  pointer-events: none;
  color: #111827;
}

/* Date + Button */
.date-field { width: 200px; }
.search-btn {
  margin-left: 8px;
  min-width: 120px;
  height: 56px;
  border-radius: 12px;
  text-transform: none;
  font-weight: 600;
  box-shadow: 0 6px 18px rgba(59, 130, 246, 0.12);
}

/* Hover effects */
.v-btn:hover:not([disabled]) { filter: brightness(0.97); }

.v-text-field:hover .v-field__outline,
.v-select:hover .v-field__outline,
.v-autocomplete:hover .v-field__outline {
  border-color: rgba(59, 130, 246, 0.22);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.06);
  transition: all 0.15s ease;
}

/* Responsive */
@media (max-width: 960px) {
  .search-card {
    gap: 10px;
    padding: 16px;
    margin: 16px;
  }
  .mode-field { width: 120px; }
  .date-field { width: 170px; }
  .search-btn { width: 100%; margin-left: 0; margin-top: 8px; }
}
</style>
