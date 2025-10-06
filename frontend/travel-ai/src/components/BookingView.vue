<template>
  <div>
    <v-expansion-panels multiple>

     <v-expansion-panel
     >
      <v-expansion-panel-title class="text-h6">
          Passenger Details
      </v-expansion-panel-title>

      <v-expansion-panel-text>
          <passenger-details
           v-model:name="name"
           v-model:email="email"
          >
  
          </passenger-details>
      </v-expansion-panel-text>
     </v-expansion-panel>
     <v-expansion-panel>
      <v-expansion-panel-title class="text-h6">
          Payment Details
      </v-expansion-panel-title>

      <v-expansion-panel-text>
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
 const onConfirmBooking = async() => {
 const res = await fetch("http://127.0.0.1:8000/book_flight", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        adults:1,
        flight_id:'1234',
        payment_details:{
            number:creditCardNumber.value,
            name:paymentName.value,
            expiry_date:expiryDate.value,
            cvv:cvv.value
        },
        
      }),
    })

    if (!res.ok) throw new Error('Network response was not ok')

    const data = await res.json()
    console.log(data)
    
}

</script>

<style>
</style>