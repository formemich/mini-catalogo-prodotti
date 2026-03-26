<script setup>
import Toast from 'primevue/toast'
import { ref, onMounted } from 'vue'
import Button from 'primevue/button'
import Menu from 'primevue/menu'
import { useRouter } from 'vue-router'

const router = useRouter()
const isDark = ref(false)
const menu = ref()

const menuItems = ref([
  {
    label: 'Prodotto semplice',
    icon: 'pi pi-tag',
    command: () => router.push('/products/new?type=simple')
  },
  {
    label: 'Prodotto con varianti',
    icon: 'pi pi-th-large',
    command: () => router.push('/products/new?type=variant')
  },
  {
    separator: true
  },
  {
    label: 'Importa da CSV',
    icon: 'pi pi-upload',
    command: () => router.push('/products/import')
  }
])

const toggleMenu = (event) => menu.value.toggle(event)

const toggleTheme = () => {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle('p-dark', isDark.value)
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

onMounted(() => {
  if (localStorage.getItem('theme') === 'dark') {
    isDark.value = true
    document.documentElement.classList.add('p-dark')
  }
})
</script>

<template>
  <div class="app-container">
    <Toast />

    <header class="app-header">
      <nav class="nav-bar">
        <router-link to="/" class="brand">
          <img src="./assets/logo.svg" alt="Logo" class="brand-logo" />
          <span class="brand-name">Mini Catalogo</span>
        </router-link>

        <div class="nav-actions">
          <Button
            :icon="isDark ? 'pi pi-sun' : 'pi pi-moon'"
            @click="toggleTheme"
            text
            rounded
            severity="secondary"
            aria-label="Toggle theme"
          />
        </div>
      </nav>
    </header>

    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}

.app-header {
  margin-bottom: 1.5rem;
  background-color: var(--p-content-background);
  border: 1px solid var(--p-content-border-color);
  border-radius: 12px;
  padding: 0.625rem 1.25rem;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  text-decoration: none;
}

.brand-logo {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  object-fit: contain;
}

.brand-name {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--p-text-color);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.app-main {
  background-color: var(--p-content-background);
  border: 1px solid var(--p-content-border-color);
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
}
</style>