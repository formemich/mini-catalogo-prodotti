<script setup>
import Toast from 'primevue/toast'
</script>

<template>
  <div class="'app-container'">
    <Toast />
    <header>
      <nav>
        <router-link to="/">Mini Catalogo</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<style scoped>
body { margin: 0; font-family: system-ui, sans-serif; background-color: #f8f9fa; }
.app-container { max-width: 1200px; margin: 0 auto; padding: 1rem; }
header { background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
nav a { text-decoration: none; color: #333; font-weight: bold; font-size: 1.2rem; }
main { background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
</style>
