<template>
  <div>
    <v-stepper v-model="step">
      <!-- Stepper Header -->
      <v-stepper-header>
        <v-stepper-item :value="1" title="Passenger Details" />
        <v-divider />
        <v-stepper-item :value="2" title="Payment Details" />
        <v-divider />
      </v-stepper-header>

      <!-- Stepper Content -->
      <v-stepper-window>
        <!-- Step 1 -->
        <v-stepper-window-item :value="1">
          <v-card class="pa-6">
            <passenger-details
              v-model:name="name"
              v-model:email="email"
            />
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="step = 2">
                Next
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-stepper-window-item>

        <!-- Step 2 -->
        <v-stepper-window-item :value="2">
          <v-card class="pa-6">
            <payment-details
             :name="name"
             :email="email"
             :total-payment="totalPayment"
            />
            <v-card-actions>
              <v-btn variant="tonal" @click="step = 1">
                Back
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                    color="primary"
                    :loading="isPaying"
                    :disabled="isPaying"
                    @click="onConfirmBooking"
                  >
                    Pay & Confirm
                  </v-btn>
            </v-card-actions>
          </v-card>
        </v-stepper-window-item>

        
        
      </v-stepper-window>
    </v-stepper>
  </div>
</template>

<script setup>
import { ref } from "vue";
import PassengerDetails from "./PassengerDetails.vue";
import PaymentDetails from "./PaymentDetails.vue";

const props = defineProps({
    flight:Object ,
 })
const step = ref(1);
const name = ref("");
const email = ref("");
const totalPayment = ref(0)
const isPaying=ref(false)

const onConfirmBooking = async () => {
  isPaying.value=true
  const res = await fetch("http://127.0.0.1:8000/start_booking", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name.value,
      email: email.value,
      adults: 1,
      id: props.flight._id,
     
    }),
  });

  if (!res.ok) throw new Error("Network response was not ok");
  const data = await res.json();

  window.location.href=data.payment_session.url
};
</script>

<style scoped>
.v-card {
  max-width: 600px;
  margin: auto;
}
</style>
