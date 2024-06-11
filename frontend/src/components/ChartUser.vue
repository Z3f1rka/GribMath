<script setup lang="ts">
import Chart from 'chart.js/auto';
import { onMounted, PropType, defineComponent, defineProps } from 'vue';

const props = defineProps({
  chartData: Array,
  chartLabels: Array
})


const data = {
      labels: props.chartLabels,
      datasets: [{
        label: 'Количество решенных примеров',
        data: props.chartData,
        borderWidth: 3,
        borderColor: '#F8B300',
        backgroundColor: 'white'
      }]}

const config = {
    type: 'line',
    data: data,
    options: {
        scales: {
            y:{
                min: 0,
            }
        }
    }
}

onMounted(() => {
    const MyChart = new Chart(
        document.getElementById('myChart'),
        config
        );
    })

</script>
<template>
    <div class="rounded-lg shadow-md grid col-span-1 bg-white border-white align justify-items-center grid-cols-1 row-span-2">
        <canvas id="myChart"></canvas>
    </div>
</template>