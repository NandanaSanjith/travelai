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
<template>
  <!-- Outer background container -->
  <div class="travel-search-wrapper d-flex align-center justify-center">
    <v-container fluid class="py-8 px-4">
      <v-row justify="center">
        <v-col cols="12" md="10" lg="8">
          <!-- Main card -->
          <v-card
            elevation="10"
            class="pa-4 d-flex flex-wrap align-center search-card"
          >
            <!-- Travel Mode -->
            <v-select
              v-model="travelType"
              :items="['Flight', 'Train', 'Bus']"
              label="Mode"
              variant="outlined"
              class="mx-2"
              hide-details
              density="comfortable"
              style="min-width: 140px"
            />

            <!-- From -->
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
              hide-details
              density="comfortable"
              style="min-width: 200px;"
            >
              <template #item="{ props: itemProps, item }">
                <v-list-item v-bind="itemProps">
                  <v-list-item-title class="font-weight-bold">
                    {{ item.raw.name }}
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-grey">
                    {{ item.raw.municipality }} - {{ item.raw.iata_code }}
                  </v-list-item-subtitle>
                </v-list-item>
              </template>
              <template #selection="{ item }">
                {{ item.raw.municipality }} ({{ item.raw.iata_code }})
              </template>
            </v-autocomplete>

            <!-- To -->
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
              hide-details
              density="comfortable"
              style="min-width: 200px;"
            >
              <template #item="{ props: itemProps, item }">
                <v-list-item v-bind="itemProps">
                  <v-list-item-title class="font-weight-bold">
                    {{ item.raw.name }}
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-grey">
                    {{ item.raw.municipality }} - {{ item.raw.iata_code }}
                  </v-list-item-subtitle>
                </v-list-item>
              </template>
              <template #selection="{ item }">
                {{ item.raw.municipality }} ({{ item.raw.iata_code }})
              </template>
            </v-autocomplete>

            <!-- Date -->
            <v-text-field
              v-model="date"
              type="date"
              label="Date"
              variant="outlined"
              hide-details
              class="mx-2"
              density="comfortable"
              style="min-width: 180px;"
            />

            <!-- Search Button -->
            <v-btn
              color="primary"
              class="ml-3 px-6 mt-2 mt-md-0"
              height="56"
              :loading="props.isLoading"
              @click="handleSearch"
              prepend-icon="mdi-magnify"
              rounded="xl"
              elevation="2"
            >
              Search
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue"

const emit = defineEmits(['onSearch'])
const travelType = ref("Flight")
const sourceCity = ref(null)
const destCity = ref(null)
const date = ref("")

const props = defineProps({
  airports: Array,
  isLoading: {
    type: Boolean,
    default: false
  }
})

const handleSearch = () => {
  if (!sourceCity.value || !destCity.value || !date.value) {
    alert("Please select From, To, and Date before searching.")
    return
  }
  const query = {
    travelType: travelType.value,
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
  return name.includes(searchText) || iataCode.includes(searchText) || municipality.includes(searchText)
}
</script>

<style scoped>
/* Gradient background */
.travel-search-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #007bff 0%, #00bcd4 100%);
  background-attachment: fixed;
  color: white;
}

/* Card style */
.search-card {
  border-radius: 20px;
  backdrop-filter: blur(10px);
  background-color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.search-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.25);
}

/* Subtle text styles */
.text-grey {
  font-size: 0.85em;
  color: #666;
}
</style>

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