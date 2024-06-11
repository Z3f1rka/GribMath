<script setup>
import { ref, reactive } from 'vue';
import Tasks from '../components/TasksMenu.vue';
import { RouterLink, useRoute } from 'vue-router';
import Task from '../components/OneTask.vue'
import { useStopwatch } from 'vue-timer-hook';



const idRoute = useRoute()["query"]["id"];

const answer = reactive({'answers' :[
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
   ['', false],
], 'time' : ''})
localStorage.setItem('answer', answer)


const autoStart = true;
const stopwatch = useStopwatch(autoStart);


const items = reactive([{ name: 'Пример 1', id: 1 }, { name: 'Пример 2', id: 2 }, { name: 'Пример 3', id: 3 }, { name: 'Пример 4', id: 4 }, { name: 'Пример 5', id: 5 }, { name: 'Пример 6', id: 6 }, { name: 'Пример 7', id: 7 }, { name: 'Пример 8', id: 8 }, { name: 'Пример 9', id: 9 }, { name: 'Пример 10', id: 10 }])


</script>


<template>
    <div class="grid grid-rows-1 grid-cols-5 shadow-md bg-white overflow-auto content-center">
        <div class="tasklist">
            <ul class="my-1">
                <div v-for="item in items" :key="item.name">
                <RouterLink :to="{ path : '/tasks', query: { id: item.id } }" @click="idRoute = item.id">
                <li class="flex">
                    <Tasks :username="item.name" />
                </li>
                </RouterLink>
                <router-view />
                </div>
                <RouterLink :to="{ path : '/end' }" @click="idRoute = item.id">
                <li class="flex" @click="answer['time'] = String(stopwatch.hours.value)+':'+String(stopwatch.minutes.value)+':'+String(stopwatch.seconds.value)">
                    <div class="rounded-lg shadow-md my-2 overflow-auto mx-5 flex " style="width: 90%;">
                        <button class="fil py-1" style="width: 100%;"><p>Завершить</p></button>
                    </div>
                </li>
                </RouterLink>
            </ul>
        </div>
        <Task :id="idRoute-1" :answer="answer['answers']" :stopwatch="stopwatch" />
    </div>
</template>
<style scoped>
.send:hover{
  background-color: #e4e4e7;
  box-shadow: inset 0 0 0 2em var(--hover);
}
html, body{
    margin: 0% !important;
}
.tasklist{
    background-color: #e2e8f0;
}
.fill {
background-color: #e2e8f0;
}
.fill:hover,
.fill:focus{
  background-color: #facc15;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.fil {
  background-color: #fbbf24;
}
.fil:hover{
  background-color: #e11d48;
  color: #525252;
  box-shadow: inset 0 0 0 2em var(--hover);
}
.fil1 {
  background-color: #fbbf24;
}
.fil1:hover{
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