<template>
  <div class="form-container">
    <h2>{{ isEdit ? 'Modifica Prodotto' : 'Nuovo Prodotto' }}</h2>
    
    <form @submit.prevent="saveProduct" class="p-fluid">
      <div class="field">
        <label for="name">Nome *</label>
        <InputText id="name" v-model="form.name" required :class="{'p-invalid': !form.name && submitted}" />
        <small v-if="!form.name && submitted" class="p-error">Il nome è obbligatorio.</small>
      </div>

      <div class="field">
        <label for="description">Descrizione</label>
        <InputText id="description" v-model="form.description" />
      </div>

      <div class="field">
        <label for="price">Prezzo *</label>
        <InputNumber id="price" v-model="form.price" mode="currency" currency="EUR" :min="0" required />
      </div>

      <div class="field">
        <label for="category">Categoria</label>
        <Select id="category" v-model="form.category_id" :options="categories" optionLabel="name" optionValue="id" placeholder="Seleziona..." />
      </div>

      <div class="field">
        <label for="tags">Tags (separati da virgola)</label>
        <InputText id="tags" v-model="tagsInput" placeholder="es: nuovo, offerta" />
      </div>

      <div class="actions">
        <Button label="Annulla" severity="secondary" @click="$router.push('/')" />
        <Button type="submit" label="Salva" :loading="saving" />
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'primevue/usetoast'
import api from '@/api'

import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Select from 'primevue/select'
import Button from 'primevue/button'

const route = useRoute()
const router = useRouter()
const toast = useToast()

const isEdit = computed(() => route.params.id !== 'new')
const categories = ref([])
const saving = ref(false)
const submitted = ref(false)

const form = ref({
  name: '',
  price: 0,
  category_id: null,
  tags:[]
})

const tagsInput = ref('')

const fetchCategories = async () => {
  const res = await api.get('/categories/')
  categories.value = res.data.results || res.data
}

const fetchProduct = async () => {
  if (!isEdit.value) return
  try {
    const res = await api.get(`/products/${route.params.id}/`)
    form.value = { ...res.data }
    tagsInput.value = (res.data.tags ||[]).join(', ')
  } catch (e) {
    toast.add({ severity: 'error', summary: 'Errore', detail: 'Prodotto non trovato', life: 3000 })
    router.push('/')
  }
}

const saveProduct = async () => {
  submitted.value = true
  if (!form.value.name || form.value.price < 0) return

  saving.value = true
  form.value.tags = tagsInput.value.split(',').map(t => t.trim()).filter(t => t)

  try {
    if (isEdit.value) {
      await api.put(`/products/${route.params.id}/`, form.value)
    } else {
      console.log('Creating product with data:', form.value)
      await api.post('/products/', form.value)
    }
    toast.add({ severity: 'success', summary: 'Successo', detail: 'Prodotto salvato', life: 3000 })
    router.push('/')
  } catch (e) {
    toast.add({ severity: 'error', summary: 'Errore', detail: 'Errore durante il salvataggio', life: 3000 })
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  fetchCategories()
  fetchProduct()
})
</script>

<style scoped>
    .form-container { 
        max-width: 600px; 
        margin: 0 auto; 
    }
    .field { 
        margin-bottom: 1.5rem; 
        display: flex; 
        flex-direction: 
        column; gap: 0.5rem; 
    }
    .actions { 
        display: flex; 
        justify-content: flex-end; 
        gap: 1rem; 
        margin-top: 2rem; 
    }
</style>