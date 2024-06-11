<script setup>
import { ref } from 'vue'
import axios from "axios"

const baseURL = import.meta.env.VITE_APP_API_URL

const isOpen = ref(false)

function closeModal() {
  isOpen.value = false
}

defineProps({
    username: String,
})

function start(){
  try {
    const { data } = axios.get(baseURL + 'examples/' + 2)
    console.log(data)
    
  } catch (err) {
    console.log(err)
  }
}

</script>

<template>
    <div class="grid grid-rows-1 grid-cols-2 overflow-auto mx-2 my-2 ml-20">
              <div @click="isOpen = !isOpen">
                <h6>• {{ username }}</h6>
              </div>
              <div class="text-right content-center">
                  <button  class="text-left" style="width: 100%;"><h4 v-if="!isOpen" style="text-align: right;">...</h4><h4 v-if="isOpen" style="text-align: right;">:</h4></button>
                </div>
              </div>
                <div class="grid grid-rows-1 grid-cols-2 overflow-auto mx-2 my-2 ml-20">
                  <transition name="slide-down-fade">
                  <div v-if="isOpen" class="text-left">
                    <ul>
                      <li class="align-center ml-10">
                        <div class="rounded-lg shadow-md my-3 border-2 overflow-auto" style="width: 80%;">
                        <button class="fill pl-20 py-1" style="width: 100%;"><p class="text-left">Легкая</p></button>
                      </div>
                      <div class="rounded-lg shadow-md my-3 border-2 overflow-auto" style="width: 80%;">
                        <button class="fill pl-20 py-1" style="width: 100%;"><p class="text-left">Средняя</p></button>
                      </div>
                      <div class="rounded-lg shadow-md my-3 border-2 overflow-auto" style="width: 80%;">
                        <button class="fill pl-20 py-1" style="width: 100%;"><p class="text-left">Высокая</p></button>
                      </div>
                      </li>
                    </ul>
                  </div>
                </transition>
                <transition name="slide-down-fade">
                <div v-if="isOpen" class="self-center"><div class="rounded-2xl shadow-md my-3 border-2 overflow-hidden" style="width: 80%; background-color: #fde047">
                        <button class="fil py-5" style="width: 100%;"><router-link :to="'/tasks?id=1'"><h6 class="text-center">Начать</h6></router-link></button>
                      </div></div>
                    </transition>
              </div>
</template>

<style scoped>
.fill:hover,
.fill:focus{
  background-color: #e4e4e7;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.fil:hover{
  background-color: #fbbf24;
  box-shadow: inset 0 0 0 2em var(--hover);
}
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
  transform: translateY(-30px)
}
.slide-down-fade-enter-active {
  transition: all 0.5s ease
}
h1{
    font-size: calc(24px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h2{
    font-size: calc(12px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
    align-content: center;
}
h3{
    font-size: calc(8px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h4{
    font-size: calc((5 + 4 * 0.7) * ((110vw - 320px) / 1280) + 2px);
    align-content: center;
}
h5{
    font-size: calc((6 + 4 * 0.7) * ((110vw - 320px) / 1280) + 3px);
    align-content: center;
}
p{
    font-size: calc((10 + 4 * 0.7) * ((110vw - 320px) / 1280) + 5px);
    align-content: center;
}
h6{
    font-size: calc((14 + 4 * 0.7) * ((110vw - 320px) / 1280) + 6px);
    align-content: center;
}
</style>