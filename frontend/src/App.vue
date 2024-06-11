<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import { onMounted, ref, provide } from 'vue'

const isDark = ref(false)

if (localStorage.getItem('userData')) {
  isDark.value = JSON.parse(localStorage.getItem('userData')).isDark._value
}

function changeTheme() {
  isDark.value = !isDark.value
  localStorage.setItem('userData', JSON.stringify({ isDark: isDark }))
}

provide('isDark', isDark)
</script>

<template>
  <div :class="isDark ? 'dark' : ''" :key="$route.fullPath">
    <div class="bg-gray-300 dark:bg-black w-full min-h-screen pt-px pb-px">
      <div class="bg-slate-100 dark:bg-gray-950 min-h-screen md:w-4/5 m-auto rounded-xl shadow-2xl mt-8 overflow-hidden">
        <Header :key="$route.fullPath">
          <li>
            <button
              @click="changeTheme"
              class="flex justify-between border-l px-3 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-neutral-300 cursor-pointer hover:text-black dark:hover:text-white"
            >
              <p>
                <img src="./images/dark_theme.svg" class="w-8" v-if="isDark" />
                <img src="./images/light_theme.svg" class="w-8" v-else />
              </p>
            </button>
          </li>
        </Header>
        <router-view> </router-view>
      </div>
    </div>
  </div>
</template>

<style></style>
