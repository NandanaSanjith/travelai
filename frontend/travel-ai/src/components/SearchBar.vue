<template> 
  <v-card elevation="8" class="pa-4 d-flex " style="border-radius: 14px;">
      <v-select
        v-model="travelType"
        :items="['Flight', 'Train', 'Bus']"
        label="Mode"
        variant="outlined"
        class="mx-2"
      />

      <v-autocomplete
        v-model="sourceCity"
        :items="props.airports"
        :custom-filter="customFilter"
        item-title="name"
        item-value="iata_code"
        clearable
        label="From"
        variant="outlined"
        class="mx-2 flex-grow-1"
        style="min-width: 250px;"
      >
       <template #item="{ props: itemProps, item }">
        <v-list-item v-bind="itemProps" :title="null" :subtitle="null">
          <v-list-item-title style="font-weight: bold;">{{ item.raw.name }}</v-list-item-title>
          <v-list-item-subtitle style="font-size: 0.85em; color: gray;">
              {{ item.raw.municipality }} - {{ item.raw.iata_code }}
          </v-list-item-subtitle>
        </v-list-item>
       </template>
       <template #selection="{ item }">
          {{ item.raw.municipality }} ({{item.raw.iata_code}})
       </template> 
      </v-autocomplete>

      <v-autocomplete
        v-model="destCity"
        :items="props.airports"
        :custom-filter="customFilter"
        item-title="name"
        item-value="iata_code"
        clearable
        label="To"
        variant="outlined"
        class="mx-2 flex-grow-1"
        style="min-width: 250px;"
      >
       <template #item="{ props: itemProps, item }">
        <v-list-item v-bind="itemProps" :title="null" :subtitle="null">
          <v-list-item-title style="font-weight: bold;">{{ item.raw.name }}</v-list-item-title>
          <v-list-item-subtitle style="font-size: 0.85em; color: gray;">
              {{ item.raw.municipality }} - {{ item.raw.iata_code }}
          </v-list-item-subtitle>
        </v-list-item>
       </template>
       <template #selection="{ item }">
          {{ item.raw.municipality }} ({{item.raw.iata_code}})
       </template> 
      </v-autocomplete>

      <v-text-field v-model="date" type="date" label="Date" variant="outlined" class="mx-2" />

      <v-btn
        color="primary"
        class="ml-3 px-6"
        height="56"
        :loading="props.isLoading"
        @click="handleSearch"
        prepend-icon="mdi-magnify"
      >
        Search
      </v-btn>
  </v-card>

   
</template>

<script setup>
import { ref, defineEmits} from "vue"

// define the events this component can emit
const emit = defineEmits(['onSearch'])
const travelType = ref("Flight")
const sourceCity = ref(null)
const destCity = ref(null)
const date = ref("")

const section = ref(null)

const props = defineProps({
    airports: Array,
    isLoading: {
      type: Boolean,
      default: false
    }

 })

const handleSearch = () => {
 //console.log(sourceCity.value,destCity.value,date.value)
 const query={
  sourceCity: sourceCity.value,
  destCity: destCity.value,
  date: date.value
 }
 emit('onSearch', query)
}

const customFilter = (value, query, item) => {
  const searchText = query.toLowerCase()
  const name = item.raw.name?.toLowerCase() || ''
  const iataCode = item.raw.iata_code?.toLowerCase() || ''
  const municipality = item.raw.municipality?.toLowerCase() || ''

  return name.includes(searchText) ||
         iataCode.includes(searchText) ||
         municipality.includes(searchText)
}
</script>

<style>
</style>