<script setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { ref } from 'vue';

let windowWidth = ref(window.innerWidth)

const isOpen = ref(false)

const items = ref([])


onMounted(async () => {
    try {
        const { data } = await axios.get('https://jsonplaceholder.typicode.com/users/?id[]=1&id[]=2&id[]=3')
        items.value = data
        items.value = [
          {"username": "Siveruhin",
          "id": 25},
          {"username": "Gennadiy",
          "id": 10},
          {"username": "Nolik",
          "id": 8}
        ]
    } catch (err) {
        console.log(err)
    }
})
</script>


<template>
    <div class="rounded-lg shadow-md bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-6">
        <div class="bg-white grid grid-rows-1 grid-cols-12 overflow-auto">
          <div v-if="windowWidth > 1100" class="col-span-7 text-center mt-16"><h6><b>Решайте, чтобы войти в таблицу лидеров!</b></h6><div class="flex justify-center"><img src="/1.jpg" class="noselect" style="width: auto; height: 18vw;"></div></div>
          <div v-if="windowWidth > 1100" class="bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-4 my-8 col-span-4">
          <ul>
          <li v-for="item in items" :key="item.id" class="align-center">
            <div class="grid grid-rows-1 grid-cols-10 overflow-auto my-4 mx-3">
              <div class="grid col-span-1 mr-1"><img src="/кубок 2.png" class="md:w-24 noselect"></div>  
          <div class="grid col-span-4 mx-5" style="align-content: center;"><p class="noselect">{{ item.username }}</p></div>
          <div class="grid col-span-4 text-right" style="align-content: center;"><h4 class="text-zinc-400 noselect">( {{ item.id }} задач решено)</h4></div>
        </div>
        <hr>
          </li>
        </ul>
        <div class="grid-rows-1 grid-cols-10 my-1 mx-5 p-1"><p class="noselect">...</p></div>
        <hr>
        <div class="grid grid-rows-1 grid-cols-10 overflow-auto my-3 mx-4 p-2">
          <div class="grid col-span-1 mr-1"><h5 class="noselect">{{ 12 }}</h5></div>  
          <div class="grid col-span-4 mx-5 noselect" style="align-content: center;"><p>Вы</p></div>
          <div class="grid col-span-4 text-right" style="align-content: center;"><h4 class="text-zinc-400 noselect">( 0 задач решено)</h4></div>
        </div>
      </div>
      <div v-if="windowWidth <= 1100" class="bg-white grid grid-rows-1 grid-cols-1 overflow-auto mx-4 my-8 col-span-12">
          <ul>
          <li v-for="item in items" :key="item.id" class="align-center">
            <div class="grid grid-rows-1 grid-cols-10 overflow-auto my-3 mx-5 p-2">
              <div class="grid col-span-1 mr-1"><img src="/cub.jpg" class="md:w-12 rounded-full noselect"></div>  
              <div class="grid col-span-1 ml-1"><img src="/cat.jpg" class="md:w-12 rounded-full noselect"></div>
          <div class="grid col-span-4 mx-5" style="align-content: center;"><p class="noselect">{{ item.username }}</p></div>
          <div class="grid col-span-4 text-right" style="align-content: center;"><h4 class="text-zinc-400 noselect">( {{ item.id }} задач решено)</h4></div>
        </div>
        <hr>
          </li>
        </ul>
        <div class="grid grid-rows-1 grid-cols-10 overflow-auto my-3 mx-5 p-2"><p class="noselect">...</p></div>
        <hr>
        <div class="grid grid-rows-1 grid-cols-10 overflow-auto my-3 mx-4 p-2">
          <div class="grid col-span-1 mr-1"><h5 class="noselect">{{ 4 }}</h5></div>  
              <div class="grid col-span-1"><img src="/cat.jpg" class="md:w-12 rounded-full noselect"></div>
          <div class="grid col-span-4 mx-5 noselect" style="align-content: center;"><p>Вы</p></div>
          <div class="grid col-span-4 text-right" style="align-content: center;"><h4 class="text-zinc-400 noselect">( 0 задач решено)</h4></div>
        </div>
      </div>
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
  transform: translateY(-30px)
}
.slide-down-fade-enter-active {
  transition: all 0.8s ease
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
    font-size: calc((12 + 4 * 0.7) * ((110vw - 320px) / 1280) + 7px);
    align-content: center;
}
</style>