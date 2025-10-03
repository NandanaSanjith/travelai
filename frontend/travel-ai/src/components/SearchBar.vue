<template> 
  <v-card elevation="8" class="pa-4 d-flex align-center" style="border-radius: 14px;">
      <v-select
        v-model="travelType"
        :items="['Flight', 'Train', 'Bus']"
        label="Mode"
        variant="outlined"
        class="mx-2"
        style="max-width: 150px;"
      />

      <v-text-field v-model="sourceCity" label="From" variant="outlined" class="mx-2 flex-grow-1" />
      <v-text-field v-model="destCity" label="To" variant="outlined" class="mx-2 flex-grow-1" />
      <v-text-field v-model="date" type="date" label="Date" variant="outlined" class="mx-2" style="max-width: 200px;" />

      <v-btn color="primary" class="ml-3 px-6" height="56" @click="handleSearch">
        🔍 Search
      </v-btn>
  </v-card>

   
</template>

<script setup>
import { ref, defineEmits} from "vue"

// define the events this component can emit
const emit = defineEmits(['onSearch'])
const travelType = ref("Flight")
const sourceCity = ref("")
const destCity = ref("")
const date = ref("")

const section = ref(null)

const handleSearch = () => {
 //console.log(sourceCity.value,destCity.value,date.value)
 const query={
  sourceCity: sourceCity.value,
  destCity: destCity.value,
  date: date.value
 }
 emit('onSearch', query)
}
</script>

<style>
</style>