<script setup>
import { ref } from 'vue';

defineProps({
    username: String,
})
</script>


<template>
    <div class="rounded-lg shadow-md my-2 overflow-auto mx-5 flex" style="width: 90%;">
        <button class="fill py-1" style="width: 100%;"><p>{{ username }}</p></button>
    </div>
</template>

<style scoped>
.fill {
background-color: white;
}
.fill:hover,
.fill:focus{
  background-color: #facc15;
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