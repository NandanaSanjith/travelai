<template>
  <div>
    <v-expansion-panels>
     <v-expansion-panel
     >
      <v-expansion-panel-title class="text-h6">
          Passenger Details
      </v-expansion-panel-title>

      <v-expansion-panel-text>
          <passenger-details>

          </passenger-details>
      </v-expansion-panel-text>
     </v-expansion-panel>
     <v-expansion-panel>
      <v-expansion-panel-title class="text-h6">
          Payment Details
      </v-expansion-panel-title>

      <v-expansion-panel-text>
          <payment-details>

          </payment-details>
      </v-expansion-panel-text>
     </v-expansion-panel>
     <v-btn class="mt-8">

        Confirm Booking
     </v-btn>
    </v-expansion-panels>
  </div>
</template>

<script setup>
 import { ref} from "vue"
 import PassengerDetails from './PassengerDetails.vue';
 import PaymentDetails from "./PaymentDetails.vue";
</script>

<style>
</style>