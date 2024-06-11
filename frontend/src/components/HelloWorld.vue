<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'

const baseURL = import.meta.env.VITE_APP_API_URL

var access_token = ref('')

if (localStorage.getItem('token')) {
  access_token.value = localStorage.getItem('token')
  console.log(access_token.value)
}

const msg = ref('')

onMounted(async () => {
  try {
    const { data } = await axios.get(baseURL)
    msg.value = data.msg
  } catch (err) {
    console.log(err)
  }
  try {
    const { data } = await axios.get(baseURL + 'protected', {
      headers: { authorization: `Bearer ${access_token.value}` }
    })
    msg.value = data.username
  } catch (err) {
    console.log(err)
  }
})
</script>

<template>
  <div class="bg-white">
    {{ msg }}
  </div>
</template>
