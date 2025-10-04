<template>
  <div>
    <v-expansion-panels>
     <v-expansion-panel
     >
      <v-expansion-panel-title class="text-h6"  @click="isPassengerViewOpen = !isPassengerViewOpen">
          Passenger Details
      </v-expansion-panel-title>

      <v-expansion-panel-text  v-show="isPassengerViewOpen">
          <passenger-details
           v-model:name="name"
           v-model:email="email"
          >
  
          </passenger-details>
      </v-expansion-panel-text>
     </v-expansion-panel>
     <v-expansion-panel>
      <v-expansion-panel-title class="text-h6"  @click="isPaymentViewOpen = !isPaymentViewOpen">
          Payment Details
      </v-expansion-panel-title>

      <v-expansion-panel-text  v-show="isPaymentViewOpen">
          <payment-details
           v-model:payment-name="paymentName"
           v-model:credit-card-number="creditCardNumber"
           v-model:cvv="cvv"
           v-model:expiry-date="expiryDate"
           >

          </payment-details>
      </v-expansion-panel-text>
     </v-expansion-panel>
     <v-btn class="mt-8"  @click="onConfirmBooking">
        Confirm Booking
     </v-btn>
    </v-expansion-panels>
  </div>
</template>

<script setup>
 import { ref} from "vue"
 import PassengerDetails from './PassengerDetails.vue';
 import PaymentDetails from "./PaymentDetails.vue";
 const name=ref('')
 const email=ref('')
 const paymentName=ref('')
 const creditCardNumber=ref('')
 const cvv=ref('')
 const expiryDate=ref('')
 const isPaymentViewOpen=ref(true)
 const isPassengerViewOpen=ref(true)
 const onConfirmBooking = () => {
  console.log(name.value)
  console.log(email.value)
  console.log(paymentName.value)
   console.log(cvv.value)
    console.log(expiryDate.value)
    console.log(creditCardNumber.value)
    
}

</script>

<style>
</style>