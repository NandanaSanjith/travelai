<template>
  <v-container class="py-6">
    <v-row justify="center" dense>
      <v-col
        v-for="flight in props.flightList"
        :key="flight.id"
        cols="12"
        md="8"
        lg="6"
      >
        <v-card elevation="5" rounded="xl" class="pa-4">
          <v-card-title class="d-flex align-center justify-space-between">
            <!-- Airline + logo -->
            <div class="d-flex align-center">
              <v-avatar size="40" class="mr-3">
                <v-img
                  :src="getAirlineLogo(flight.airline)"
                  alt="airline logo"
                  cover
                />
              </v-avatar>
              <div>
                <div class="text-h6 font-weight-medium">
                  {{ flight.airline }}
                </div>
                <div class="text-body-2 text-medium-emphasis">
                  {{ flight.departure_city }} → {{ flight.arrival_city }}
                </div>
              </div>
            </div>

            <!-- Price chip -->
            <v-chip color="primary" size="small" variant="flat">
              ₹{{ flight.price }}
            </v-chip>
          </v-card-title>

          <!-- Flight details -->
          <v-card-text>
            <v-row>
              <v-col cols="12" sm="6">
                <v-icon size="small" color="primary" class="mr-1">
                  mdi-calendar
                </v-icon>
                {{ flight.departure_date }}
              </v-col>

              <v-col cols="12" sm="6">
                <v-icon size="small" color="primary" class="mr-1">
                  mdi-seat
                </v-icon>
                Seats available: {{ flight.available_seats }}
              </v-col>
            </v-row>
          </v-card-text>

          <!-- Book button -->
          <v-card-actions class="justify-end">
            <v-btn
              color="primary"
              variant="elevated"
              prepend-icon="mdi-ticket-confirmation"
              @click="onClickEvent(flight)"
            >
              Book Now
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
const emit = defineEmits(['showBookingView']);
const props = defineProps({
    flightList: Array ,
 })

const onClickEvent = (flight) => {
  emit('showBookingView', flight);
};

// Airline logos mapping
const getAirlineLogo = (airline) => {
  const logos = {
    'IndiGo': '../assets/indigo.svg',
    'Air India': '../assets/Air_India.svg',
    'SpiceJet': '../assets/SpiceJet_logo.svg',
    'AirAsia': '../assets/AirAsia_New_Logo.svg',
  };
  return logos[airline] || 'https://cdn-icons-png.flaticon.com/512/3076/3076129.png'; // default airplane icon
};
</script>
