<script setup>
import User from '../components/User.vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { onMounted, ref } from 'vue'

const route_id = useRoute()['query']['id']

const items = ref([])

const baseURL = import.meta.env.VITE_APP_API_URL

const user_id = ref('')
const email = ref('')
const name = ref('')
const chartData = ref([])
const chartLabels = ref([])
const display = ref(false)

onMounted(async () => {
  try {
    const { data } = await axios.get(baseURL + 'profile/' + route_id)
    items.value = data
    console.log(data)
    user_id.value = data.id
    email.value = data.email
    name.value = data.username
    chartData.value = data.data
    chartData.value[31] = 4
    chartLabels.value = data.labels
    display.value = true
    console.log(chartData.value)
  } catch (err) {
    console.log(err)
  }
})
</script>

<template>
<div>
    <div v-if="display" class="mt-4">
      <User
        user-img="/avatar.png"
        :email="email"
        :name="name"
        :chartData="chartData"
        :chartLabels="chartLabels"
        :count="4"
      />
    </div>
    <div v-else></div>
  </div>
</template>
