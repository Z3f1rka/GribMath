<script setup>
import { ref } from 'vue'
import ChartUser from './ChartUser.vue'

let windowWidth = ref(window.innerWidth)

const height = ref('grid grid-rows-1 grid-cols-5 overflow-auto mx-6')

if (windowWidth.value > 750) {
  height.value = 'grid grid-rows-1 grid-cols-5 overflow-auto mx-6 my-6'
}

defineProps({
  name: String,
  userImg: String,
  count: Number,
  email: String,
  chartData: Array,
  chartLabels: Array
})
</script>

<template>
  <div class="gap-y-8">
    <div v-if="windowWidth < 750">
      <div class="rounded-lg shadow-md bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-6">
        <div :class="height">
          <div class="grid bg-white border-white align justify-items-start items-center">
            <img :src="userImg" class="md:w-50 rounded-full" />
          </div>
          <div
            class="v-resize-text p-5 bg-white border-white mt-1 col-span-4 content-center pt-10 mb-3"
          >
            <h1>
              <b>{{ name }}</b>
            </h1>
            <h2>{{ email }}</h2>
          </div>
        </div>
      </div>
      <div class="grid grid-rows-1 grid-cols-1 overflow-auto mx-6 mt-4">
        <div class="grid grid-rows-1 grid-cols-1 overflow-auto pb-4 gap-4">
          <div class="rounded-lg shadow-md p-5 bg-white border-white">
            <h6><b>За сегодня вы решили:</b></h6>
            <h6><b>Ваша цель:</b></h6>
          </div>
          <!-- <ChartUser /> -->
        </div>
      </div>
    </div>
    <div v-if="windowWidth > 750">
      <div class="rounded-lg shadow-md bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-6">
        <div :class="height">
          <div class="grid bg-white border-white align justify-items-start items-center">
            <img :src="userImg" class="md:w-50 rounded-full" />
          </div>
          <div
            class="v-resize-text p-5 bg-white border-white mt-1 col-span-4 content-center pt-10 mb-3"
          >
            <h1>
              <b>{{ name }}</b>
            </h1>
            <h2>{{ email }}</h2>
          </div>
        </div>
      </div>
      <div class="grid grid-rows-1 grid-cols-1 overflow-auto mx-6 mt-4">
        <div v-if="windowWidth > 750" class="grid grid-rows-2 grid-cols-2 overflow-auto pb-4 gap-4">
          <div class="grid grid-rows-2 grid-cols-1">
            <div>
              <div class="rounded-lg shadow-md p-5 bg-white border-white">
                <p><b>За сегодня вы решили: {{ count }}</b></p>
              </div>
            </div>
          </div>
          <ChartUser :chart-data="chartData" :chart-labels="chartLabels"/>
        </div>
        <div>
          <div v-if="windowWidth > 750">
            <!-- <ChartUser :chart-data="chartData" :chart-labels="chartLabels"/> -->
          </div>
        </div>
      </div>
      <div v-if="windowWidth <= 750" class="grid grid-rows-1 grid-cols-1 overflow-auto pb-4 gap-4">
        <div>
          <div
            v-if="windowWidth <= 750"
            class="rounded-lg shadow-md p-5 bg-white border-white col-span-2"
          >
            <h3><b>За сегодня вы решили:</b></h3>
            <h3><b>Ваша цель:</b></h3>
          </div>
          <div
            v-if="windowWidth <= 750"
            class="rounded-lg shadow-md p-5 mt-5 bg-white border-white col-span-2"
          >
            <h3><b>За сегодня вы решили:</b></h3>
            <h3><b>Ваша цель:</b></h3>
            <p>{{ id }}</p>
          </div>
        </div>
        <div>
          <div class="col-span-2" v-if="windowWidth <= 750">
            <ChartUser />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.send:hover {
  background-color: #e4e4e7;
  box-shadow: inset 0 0 0 2em var(--hover);
}
html,
body {
  margin: 0% !important;
}
.tasklist {
  background-color: #e2e8f0;
}
.fill {
  background-color: #e2e8f0;
}
.fill:hover,
.fill:focus {
  background-color: #facc15;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.fil {
  background-color: #fbbf24;
}
.fil:hover {
  background-color: #e11d48;
  color: #525252;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.fil1 {
  background-color: #fbbf24;
}
.fil1:hover {
  background-color: #84cc16;
  color: #525252;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.noselect {
  cursor: default;
  -webkit-user-select: none;
  -webkit-touch-callout: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
}

.noselect:focus {
  outline: none;
}
.slide-down-fade-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}
.slide-down-fade-enter-active {
  transition: all 0.5s ease;
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
h6 {
  font-size: calc((14 + 4 * 0.7) * ((110vw - 320px) / 1280) + 6px);
  align-content: center;
}
</style>
