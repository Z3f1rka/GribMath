<script setup>

</script>


<template>
    <div class="rounded-lg shadow-md bg-white dark:bg-gray-900 grid grid-rows-1 grid-cols-3 overflow-auto mx-6 my-5 p-5 pt-10 content-center text-center">
      <div class="flex justify-center">
        <img
          src="/lamp_dark.png"
          class="noselect"
          style="width: auto; height: 18vw"
          v-if="isDark"
        /><img src="/end.jpg" class="noselect" style="width: auto; height: 18vw" v-else />
      </div>
      <div class="self-center col-span-2 dark:text-slate-100">
        <h2><b>Поздравляю вы решили 4/10 примеров!</b></h2>
      </div>
      <RouterLink :to="{ path : '/profi1e', query: { id: 6 } }" >
      <div class="rounded-lg shadow-md my-2 overflow-auto mx-5 flex mt-5" style="width: 90%;">
        <button class="fill py-1" style="width: 100%;"><p>На профиль</p></button>
    </div>
    </RouterLink>
      </div>
</template>

<style scoped>
.fill {
  background-color: #e2e8f0;
}
.fill:hover,
.fill:focus {
  background-color: #facc15;
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