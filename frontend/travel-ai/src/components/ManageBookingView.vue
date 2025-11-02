<template>
 <div>
   <!-- Booking & Payment Status -->
   <v-row class="mb-4">
     <v-col cols="6">
       <v-card flat color="blue-lighten-5" class="pa-3" elevation="2" rounded="lg">
         <div class="text-caption text-grey-darken-1 font-weight-bold">Booking Status</div>
         <v-chip
           :color="getStatusColor(bookingData.booking_details.booking_status)"
           class="mt-2"
         >
           {{ bookingData.booking_details.booking_status.toUpperCase() }}
         </v-chip>
       </v-card>
     </v-col>
     <v-col cols="6">
       <v-card flat color="green-lighten-5" class="pa-3" elevation="2" rounded="lg">
         <div class="text-caption text-grey-darken-1 font-weight-bold">Payment Status</div>
         <v-chip
           :color="getStatusColor(bookingData.payment_details.payment_status)"
           class="mt-2"
         >
           {{ bookingData.payment_details.payment_status.toUpperCase() }}
         </v-chip>
       </v-card>
     </v-col>
   </v-row>


   <!-- Flight Details -->
   <v-card
     color="grey-lighten-5"
     flat
     rounded="lg"
     class="pa-4 mb-4 text-left"
     elevation="2"
   >
     <h3 class="text-h6 mb-3">Flight Details</h3>
     <v-row dense>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Flight Number</div>
         <div class="font-weight-bold">{{ bookingData.flight_details.flight_id }}</div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Airline</div>
         <div class="font-weight-bold">{{ bookingData.flight_details.airline }}</div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">From</div>
         <div class="font-weight-bold text-capitalize">
           {{ bookingData.flight_details.departure_city }}
           (<span class="text-uppercase">{{ bookingData.flight_details.departure_city_iata }}</span>)
         </div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">To</div>
         <div class="font-weight-bold text-capitalize">
           {{ bookingData.flight_details.arrival_city }}
           (<span class="text-uppercase">{{ bookingData.flight_details.arrival_city_iata }}</span>)
         </div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Departure</div>
         <div class="font-weight-bold">{{ bookingData.flight_details.departure_time }}</div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Arrival</div>
         <div class="font-weight-bold">{{ bookingData.flight_details.arrival_time }}</div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Date</div>
         <div class="font-weight-bold">{{ bookingData.flight_details.departure_date }}</div>
       </v-col>
       <v-col cols="6">
         <div class="text-caption text-grey-darken-1">Price</div>
         <div class="font-weight-bold">₹{{ bookingData.flight_details.price }}</div>
       </v-col>
     </v-row>
   </v-card>


   <!-- Passenger Details -->
   <v-card
     v-if="bookingData.booking_details.passenger_details && bookingData.booking_details.passenger_details.length > 0"
     color="grey-lighten-5"
     flat
     rounded="lg"
     class="pa-4 mb-4 text-left"
     elevation="2"
   >
     <h3 class="text-h6 mb-3">Passenger Details</h3>
     <v-list density="compact" bg-color="transparent">
       <v-list-item
         v-for="(passenger, index) in bookingData.booking_details.passenger_details"
         :key="index"
         class="mb-2"
       >
         <v-list-item-title>
           <v-icon size="small" class="mr-2">mdi-account</v-icon>
           {{ passenger.name }}
         </v-list-item-title>
         <v-list-item-subtitle>
           <v-chip size="x-small" class="ml-8">{{ passenger.gender }}</v-chip>
         </v-list-item-subtitle>
       </v-list-item>
     </v-list>
   </v-card>
 </div>
</template>


<script setup>
const props = defineProps({
 bookingData: {
   type: Object,
   required: true
 }
});


const getStatusColor = (status) => {
 const statusMap = {
   'pending': 'warning',
   'confirmed': 'success',
   'completed': 'success',
   'cancelled': 'error',
   'failed': 'error'
 };
 return statusMap[status.toLowerCase()] || 'grey';
};
</script>

