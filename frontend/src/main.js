import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'
import { definePreset } from '@primevue/themes';
import 'primeicons/primeicons.css'

import ToastService from 'primevue/toastservice'
import ConfirmationService from 'primevue/confirmationservice'

const app = createApp(App)

const auraBluePreset = definePreset(Aura, {
    semantic: {
        primary: {
            50:  '#eff6ff',
            100: '#dbeafe',
            200: '#bfdbfe',
            300: '#93c5fd',
            400: '#60a5fa',
            500: '#3b82f6',
            600: '#2563eb',
            700: '#1d4ed8',
            800: '#1e40af',
            900: '#1e3a8a',
            950: '#172554'
        }
    }
});

app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: auraBluePreset,
         options: {
            darkModeSelector: '.p-dark'
        }
    }
})
app.use(ToastService)
app.use(ConfirmationService)


app.mount('#app')
