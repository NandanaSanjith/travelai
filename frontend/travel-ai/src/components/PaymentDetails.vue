<template>
    <div>
        <v-text-field
         label="Name" 
         v-model="localPaymentName" 
         @input="emit('update:paymentName', localPaymentName)"
        ></v-text-field>

        <v-text-field 
        label="Credit Card Number"  
        v-model="localCreditCardNumber"
        @input="emit('update:creditCardNumber', localCreditCardNumber)"
        ></v-text-field>

        <v-text-field 
        label="cvv" 
         v-model="localCvv"
         @input="emit('update:cvv', localCvv)"

         ></v-text-field>

        <v-text-field 
          v-model="localExpiryDate" 
          type="date"
          label="Date"
          variant="outlined"
          class="mx-2" 
          style="max-width: 200px;"
          @input="emit('update:expiryDate', localExpiryDate)"
        />

    </div>
</template>

<script setup>
 import {ref,defineEmits} from 'vue'
 const emit = defineEmits(['update:paymentName',
  'update:creditCardNumber',
  'update:cvv',
  'update:expiryDate'])

 defineProps({
   paymentName:String ,
   creditCardNumber:String,
   cvv:String,
   expiryDate:String
 })
 const localPaymentName=ref('')
 const localCreditCardNumber=ref('')
 const localCvv=ref('')
 const localExpiryDate=ref('')
</script>

<style>
</style>