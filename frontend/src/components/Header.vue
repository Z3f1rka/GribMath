<script setup>
import { inject, onMounted, ref } from 'vue'
import axios from 'axios'
import router from '@/router'

var isDark = inject('isDark')

var access_token = ref('')
var refresh_token = ref('')

if (localStorage.getItem('token')) {
  access_token.value = localStorage.getItem('token')
}
if (localStorage.getItem('refresh_token')) {
  refresh_token.value = localStorage.getItem('refresh_token')
}

var isNotAuth = ref(
  access_token.value == '' ||
    access_token.value == 'null' ||
    access_token.value == 'undefined' ||
    access_token.value == null
)

const baseURL = import.meta.env.VITE_APP_API_URL

var id = ref(0)

onMounted(async () => {
  try {
    const { data } = await axios.get(baseURL + 'protected', {
      headers: { authorization: `Bearer ${access_token.value}` }
    })
    id.value = parseInt(data.id)
    isNotAuth.value = false
  } catch (err) {
    console.log(err)
    try {
      const { data } = await axios.post(baseURL + 'refresh', {
        headers: { authorization: `Bearer ${refresh_token.value}` }
      })
      localStorage.setItem('token', data.access_token)
      access_token.value = data.access_token
      localStorage.setItem('refresh_token', data.refresh_token)
      refresh_token.value = data.refresh_token_token
      isNotAuth.value = false
    } catch (err) {
      console.log(err)
      localStorage.setItem('token', null)
      localStorage.setItem('refresh_token', null)
      isNotAuth.value =
        access_token.value == '' ||
        access_token.value == 'null' ||
        access_token.value == 'undefined' ||
        access_token.value == null
      isNotAuth.value = true
    }
  }
})

function logout() {
  localStorage.setItem('token', null)
  localStorage.setItem('refresh_token', null)
  isNotAuth.value =
    access_token.value == '' ||
    access_token.value == 'null' ||
    access_token.value == 'undefined' ||
    access_token.value == null
  isNotAuth.value = true
  router.push('/')
  window.location.reload()
}

function goProfile() {
  router.push({ path: '/profile', query: { id: id.value } })
}
</script>

<template>
  <header
    class="flex justify-between border-b bg-white dark:bg-zinc-950 dark:text-white border-slate-300 dark:border-slate-800 items-center py-3"
  >
    <div class="pl-5">
      <router-link to="/">
        <img src="@/images/logo_dark.svg" alt="logo" class="h-16" v-if="isDark" />
        <img src="@/images/logo.svg" alt="logo" class="h-16" v-else />
      </router-link>
    </div>
    <ul class="flex justify-between" :key="id">
      <li v-if="isNotAuth" key="1">
        <button
          class="flex justify-between border-l px-3 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-neutral-300 cursor-pointer hover:text-black dark:hover:text-white"
        >
          <router-link :to="'/login'">
            <p>Вход</p>
          </router-link>
        </button>
      </li>
      <li v-else>
        <button
          @click="goProfile"
          class="flex justify-between border-l px-3 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-neutral-300 cursor-pointer hover:text-black dark:hover:text-white"
        >
          Профиль
        </button>
      </li>
      <li v-if="isNotAuth" key="3">
        <button
          class="flex justify-between border-l px-3 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-neutral-300 cursor-pointer hover:text-black dark:hover:text-white"
        >
          <router-link :to="'/register'">
            <p>Регистрация</p>
          </router-link>
        </button>
      </li>
      <li v-else key="4">
        <button
          @click="logout"
          class="flex justify-between border-l px-3 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-neutral-300 cursor-pointer hover:text-black dark:hover:text-white"
        >
          <p>Выход</p>
        </button>
      </li>
      <slot> </slot>
    </ul>
  </header>
</template>
