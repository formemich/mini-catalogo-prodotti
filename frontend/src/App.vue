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
  .app-container { 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 1rem; 
  }
  header { 
    padding: 1rem; 
    margin-bottom: 1rem; 
  }
  nav a { 
    text-decoration: none; 
    color: #ffffff; 
    font-weight: bold; 
    font-size: 1.2rem; 
  }
  main { 
    padding: 1.5rem; 
    border-radius: 8px;
    }
</style>
