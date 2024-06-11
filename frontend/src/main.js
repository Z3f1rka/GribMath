import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {VueMathjax} from 'vue-mathjax'
import katexvue3 from "katex-vue3";
import './index.css'

const app = createApp(App)



app.use(router).use(katexvue3, {
    flag: [
      
    ],
    options: {
      displayMode: false, 
      throwOnError: false, 
      errorColor: "#FF0000" 
    }
  })

app.mount('#app')
