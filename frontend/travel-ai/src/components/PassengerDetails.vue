<template>
 <div>
  <v-text-field 
   label="Name"
   v-model="localName"
   @input="emit('update:name', localName)"

 >
  </v-text-field>
  <v-text-field 
   label="Email"
   v-model="localEmail"
   @input="emit('update:email', localEmail)"

  >
  </v-text-field>


 </div>
</template>

<script setup>
 import {ref} from 'vue'
 defineProps({
    name:String ,
    email:String
 })
 const localName=ref('')
 const localEmail=ref('')
</script>

<style>
</style>