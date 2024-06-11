<script setup>
import Theme from '../components/Theme.vue'
import leaderboard from '../components/leaderboard.vue'
import axios from 'axios'
import { onMounted, inject } from 'vue'
import { ref } from 'vue'


const baseURL = import.meta.env.VITE_APP_API_URL

const items = ref([])
const authorization = ref(false)

var isDark = inject('isDark')

var access_token = ref('')

if (localStorage.getItem('token')) {
  access_token.value = localStorage.getItem('token')}

var isNotAuth = ref(
  access_token.value == '' ||
    access_token.value == 'null' ||
    access_token.value == 'undefined' ||
    access_token.value == null
)

onMounted(async () => {
  try {
    if (!(isNotAuth.value)){
    const { data } = await axios.get(
      baseURL + "all_categories"
    )
    items.value = data
    console.log(items.value)
  }
    }catch (err) {
    console.log(err)
  }
})
</script>

<template>
  <div v-if="isNotAuth" class="mt-4">
    <div
      class="rounded-lg shadow-md bg-white dark:bg-gray-900 grid grid-rows-1 grid-cols-3 overflow-auto mx-6 my-5 p-5 pt-10 content-center text-center"
    >
      <div class="flex justify-center">
        <img
          src="/lamp_dark.png"
          class="noselect"
          style="width: auto; height: 18vw"
          v-if="isDark"
        /><img src="/lamp.jpeg" class="noselect" style="width: auto; height: 18vw" v-else />
      </div>
      <div class="self-center col-span-2 dark:text-slate-100">
        <h2><b>Войдите или зарегистрируйтесь, чтобы начать решать!</b></h2>
      </div>
    </div>
  </div>
  <div class="mt-4" v-else>
    <leaderboard />
    <div
      class="rounded-lg shadow-md bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-6 my-5 p-5"
    >
      <h3 class="text-center">Выберите категорию и сложность</h3>
      <ul>
        <li v-for="item in items" :key="item.id">
          <Theme :username="item.title" />
          <hr />
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.noselect {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.slide-down-fade-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}
.slide-down-fade-enter-active {
  transition: all 0.8s ease;
}
h1 {
  font-size: calc(24px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h2 {
  font-size: calc(12px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
  align-content: center;
}
h3 {
  font-size: calc(8px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h4 {
  font-size: calc((5 + 4 * 0.7) * ((110vw - 320px) / 1280) + 2px);
  align-content: center;
}
h5 {
  font-size: calc((6 + 4 * 0.7) * ((110vw - 320px) / 1280) + 3px);
  align-content: center;
}
p {
  font-size: calc((10 + 4 * 0.7) * ((110vw - 320px) / 1280) + 5px);
  align-content: center;
}
</style>
