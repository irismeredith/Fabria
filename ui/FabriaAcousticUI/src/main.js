// The main app file that executes on load. It currently uses the pinia and vuetify plugins

// Author: Iris Meredith

// Last modified: 27/12/2023


// Imports

import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


// Create plugins

const vuetify = createVuetify({
  components,
  directives,
})

const pinia = createPinia()

// Create and mount the app

createApp(App).use(pinia).use(vuetify).mount('#app')
