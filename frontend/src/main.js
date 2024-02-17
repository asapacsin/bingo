import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

import axios from 'axios'
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8001/'

createApp(App).mount('#app')
