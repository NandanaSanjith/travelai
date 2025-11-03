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
             <h3 class="text-h6 mb-4">Enter Booking Person Details</h3> 
             <booking-person-details v-model:name="name" v-model:email="email" />
          </v-card>
          <v-card class="pa-6">
            <h3 class="text-h6 mb-4">Enter Passenger Details</h3>

            <div v-for="(passenger, index) in passengers" :key="index" class="mb-4">
              <v-card class="pa-4 mb-3" outlined>
                <h4 class="text-subtitle-1 mb-3">Passenger {{ index + 1 }}</h4>

                <v-text-field
                  label="Name"
                  v-model="passenger.name"
                  placeholder="Enter passenger name"
                  outlined
                ></v-text-field>

                <v-select
                  label="Identification Type"
                  :items="['Passport', 'Aadhar', 'Driver\'s License']"
                  v-model="passenger.identification_type"
                  outlined
                ></v-select>

                <v-text-field
                  label="Identification Number"
                  v-model="passenger.identification_number"
                  placeholder="Enter ID number"
                  outlined
                ></v-text-field>
              </v-card>
            </div>

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
import { ref, onMounted } from "vue";
import PaymentDetails from "./PaymentDetails.vue";
import BookingPersonDetails from "./BookingPersonDetails.vue";
const props = defineProps({
  flight: Object,
  adults: Number,
});

const step = ref(1);
const name = ref("");
const email = ref("");
const totalPayment = ref(0);
const isPaying = ref(false);

// Create passenger details array based on number of adults
const passengers = ref([]);

onMounted(() => {
  totalPayment.value = props.flight.price * props.adults;

  // Initialize passenger objects
  passengers.value = Array.from({ length: props.adults }, () => ({
    name: "",
    identification_type: "",
    identification_number: "",
  }));
});

const onConfirmBooking = async () => {
  isPaying.value = true;

  try {
    const res = await fetch("http://127.0.0.1:8000/start_booking", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        adults: props.adults,
        id: props.flight._id,
        passenger_details: passengers.value, // ✅ send all passengers here
      }),
    });

    if (!res.ok) throw new Error("Network response was not ok");
    const data = await res.json();
    window.location.href = data.payment_session.url;
  } catch (error) {
    console.error("Booking failed:", error);
  } finally {
    isPaying.value = false;
  }
};
</script>

<style scoped>
.v-card {
  max-width: 600px;
  margin: auto;
}
</style>
