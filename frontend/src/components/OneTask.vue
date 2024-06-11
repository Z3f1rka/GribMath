<script setup>
import { ref, reactive } from 'vue';

defineProps({
    id: String,
    answer: Array,
    stopwatch: Array,
})


var list = reactive({
    1: ['-4~*~-83', '332', 'Посчитать -4 * -83'],
    2: ['3~*~9~+~32~/~4', '35', 'Перемножаем 9 и 3;Делим 32 на 4;Складываем 8 и 27;'],
    3: ['45~/~-5~+~3~+~8', '2', 'Делим 45 на -5;Складываем 3 и -9;Складываем 8 и -6;'],
    4: ['(~33~/~11~)~*~9', '27', 'Делим 33 на 11;Перемножаем 9 и 3;'],
    5: ['348~/~87', '4', 'Посчитать 348 / 87'],
    6: ['8~*~(~-5~+~7~)', '16', 'Складываем 7 и -5;Перемножаем 2 и 8;'],
    7: ['32~/~-8~-~9~*~8', '-76', 'Делим 32 на -8;Перемножаем 8 и 9;Вычитаем 72 из -4;'],
    8: ['55~/~-11~-~8~-~8', '-21', 'Делим 55 на -11;Вычитаем 8 из -5;Вычитаем 8 из -13;'],
    9: ['-5~-~(~-2~*~-4~)', '-13', 'Перемножаем -4 и -2;Вычитаем 8 из -5;'],
    10: ['90~/~-45', '-2', 'Посчитать 90 / -45'],
})


function html(text){
    return katex.renderToString(text)
}


</script>

<template>
    <div class="grid col-span-4">
            <div>
                <div class="grid grid-rows-1 grid-cols-2">
                    <div>
                        <h6 class="ml-5 mt-2"><b>Числовые примеры - Средние</b></h6>
                    </div>
                    <div class="text-right m-5">
                    </div>
                </div>
            <p class="text-center mt-5"><b>Пример {{ id+1 }} </b></p>
            <div class="text-center my-5" v-katex:display="html(list[id+1][0])"></div>
            <div class="text-center grid grid-rows-1 grid-cols-8">
                <div class="grid">
                    <p>Ответ :</p>
                </div>
                <div v-if='!(answer[id][0] != "" && answer[id][0] != null)' class="grid col-span-5">
                    <input v-model="msg" type="input" class="border-2 rounded-lg" style="width: 100%;">
                </div>
                <div v-if='answer[id][0] != "" && answer[id][0] != null' class="grid col-span-6">
                    <input v-model="msg" type="input" class="border-2 rounded-lg" style="width: 100%;">
                </div>
                <div class="grid col-span-2">
                    <div v-if="answer[id][0] == '' || answer[id][0] == null" class="rounded-lg shadow-md overflow-auto mx-5 border-2" style="width: 70%;">
                        <button class="fil1 py-1" style="width: 100%;" @click="answer[id][0] = msg"><p>Отправить</p></button>
                    </div>
                </div>
            </div>
            <div v-if='!(answer[id][0] != "" && answer[id][0] != null)'><p class="mx-8 mt-5">В ответ запишите только целое число, при необходимости округлите до сотых</p></div>
            <transition name="slide-down-fade">
                <div v-if='answer[id][0] != "" && answer[id][0] != null'>
                    <div v-if="answer[id][0] === list[id+1][1]" hidden>
                        {{ answer[id][1] = true }}
                    </div>
                    <div v-if="answer[id][1] == true">
                        <p class="mx-8 mt-5 mb-1">Верно!</p>
                    </div>
                    <div v-else>
                        <p class="mx-8 mt-5 mb-1">Неверно!</p>
                    </div>
                    <div>
                        <p class="mx-8 mt-5 mb-1">
                            <b>Решение: </b>
                        </p>
                        <div class="ml-8 text-left" v-katex:display="html(list[id+1][1])" ></div>
                    </div>
                    <div>
                        <p class="mx-8 mt-5 mb-1">
                            <b>Шаги решения: </b>
                        </p>
                        <div v-for="item in (list[id+1][2].split(';'))" class="ml-8 text-left">
                            <div class="my-1">{{ item }}</div>
                        </div>
                    </div>
            </div>
        </transition>
        </div>
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