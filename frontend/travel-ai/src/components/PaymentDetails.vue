<template>
    <div>
       <v-card class="pa-6">
         <h3 class="text-h6 mb-4">Payment Details</h3>
         <p><strong>Name:</strong> {{ name }}</p>
         <p><strong>Email:</strong> {{ email }}</p>
         <p><strong>Total Payment:</strong> {{ totalPayment }}</p>
           
            
        </v-card>
    </div>
</template>

<script setup>
 import {ref,defineEmits} from 'vue'
 
 defineProps({
   name:String ,
   email:String,
   totalPayment:Number,
 })

</script>

<style>
</style>