<template>
    <div>
        <div class="header-actions">
            <h1>Prodotti</h1>
            <Button label="Nuovo Prodotto" icon="pi pi-plus" @click="$router.push('/product/new')" />
        </div>

        <div class="filters">
          <InputText v-model="filters.search" placeholder="Cerca per nome..." />
          <Select v-model="filters.category" :options="categories" optionLabel="name" optionValue="id" placeholder="Categoria" showClear />
          <InputNumber v-model="filters.min_price" placeholder="Prezzo Min" mode="currency" currency="EUR" @input="filters.min_price = $event.value" />
          <InputNumber v-model="filters.max_price" placeholder="Prezzo Max" mode="currency" currency="EUR" @input="filters.max_price = $event.value" />
        </div>
        
        <DataTable :value="products" lazy :totalRecords="totalRecords" :loading="loading"
               @page="onPage" @sort="onSort"
               paginator :rows="10" :rowsPerPageOptions="[5, 10, 20]"
               responsiveLayout="scroll">
      
        <Column field="name" header="Nome" sortable></Column>
        <Column field="price" header="Prezzo" sortable>
            <template #body="{ data }">€ {{ data.price }}</template>
        </Column>

        <Column field="description" header="Descrizione">
            <template #body="{ data }">
            {{ data.description ? (data.description.length > 50 ? data.description.substring(0, 50) + '...' : data.description) : 'Nessuna' }}
            </template>
        </Column>

        <Column field="category_id" header="Categoria">
            <template #body="{ data }">
            {{ getCategoryName(data.category_id) }}
            </template>
        </Column>

        <Column field="tags" header="Tags">
            <template #body="{ data }">
            {{ data.tags && data.tags.length > 0 ? data.tags.join(', ') : 'Nessuna' }}
            </template>
        </Column>

        <Column field="created_at" header="Creato il" sortable>
            <template #body="{ data }">
            {{ new Date(data.created_at).toLocaleDateString() }}
            </template>
        </Column>

        <Column header="">
            <template #body="{ data }">
            <Button icon="pi pi-pencil" text @click="$router.push(`/product/${data.id}`)" />
            <Button icon="pi pi-trash" severity="danger" text @click="deleteProduct(data.id)" />
            </template>
        </Column>

        </DataTable>
    </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useToast } from 'primevue/usetoast'
import { useConfirm } from 'primevue/useconfirm'
import api from '@/api'

import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Select from 'primevue/select'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

const toast = useToast()
const confirm = useConfirm()
const products = ref([])
const categories = ref([])
const loading = ref(false)
const totalRecords = ref(0)

const filters = ref({ search: '', category: null, min_price: null, max_price: null })
let timeoutId = null
watch(filters, () => {
  clearTimeout(timeoutId)
  timeoutId = setTimeout(() => {
    lazyParams.value.page = 1
    fetchProducts()
  }, 10)
}, { deep: true })
const lazyParams = ref({ page: 1, ordering: '', page_size: 10})

const fetchCategories = async () => {
  try {
    const res = await api.get('/categories/')
    categories.value = res.data.results || res.data 
  } catch (e) {
    toast.add({ severity: 'error', summary: 'Errore', detail: 'Impossibile caricare le categorie', life: 3000 })
  }
}

const fetchProducts = async () => {
  loading.value = true
  try {
    const params = {
      page: lazyParams.value.page,
      page_size: lazyParams.value.page_size,
      ordering: lazyParams.value.ordering,
    }
    
    if (filters.value.search) params.search = filters.value.search
    if (filters.value.category) params.category_id = filters.value.category
    if (filters.value.min_price !== null) params.min_price = filters.value.min_price
    if (filters.value.max_price !== null) params.max_price = filters.value.max_price

    const res = await api.get('/products/', { params })
    products.value = res.data.results || res.data
    totalRecords.value = res.data.count || res.data.length
  } catch (e) {
    if (e.response && e.response.status === 404 && lazyParams.value.page > 1) {
      lazyParams.value.page = 1
      fetchProducts()
    } else {
      toast.add({ severity: 'error', summary: 'Errore', detail: 'Errore nel caricamento prodotti', life: 3000 })
    }
  } finally {
    loading.value = false
  }
}

const onPage = (event) => {
  lazyParams.value.page = event.page + 1
  lazyParams.value.page_size = event.rows
  fetchProducts()
}

const onSort = (event) => {
  const prefix = event.sortOrder < 0 ? '-' : ''
  lazyParams.value.ordering = `${prefix}${event.sortField}`
  fetchProducts()
}

const deleteProduct = (id) => {
  confirm.require({
    message: 'Sei sicuro di voler eliminare questo prodotto?',
    header: 'Conferma Eliminazione',
    icon: 'pi pi-exclamation-triangle',
    rejectProps: {
      label: 'Annulla',
      severity: 'secondary',
      outlined: true
    },
    acceptProps: {
      label: 'Elimina',
      severity: 'danger'
    },
    accept: async () => {
      try {
        await api.delete(`/products/${id}/`)
        toast.add({ severity: 'success', summary: 'Successo', detail: 'Prodotto eliminato', life: 3000 })
        
        if (products.value.length === 1 && lazyParams.value.page > 1) {
          lazyParams.value.page--
        }
        
        fetchProducts()
      } catch (e) {
        toast.add({ severity: 'error', summary: 'Errore', detail: 'Errore durante l\'eliminazione', life: 3000 })
      }
    }
  })
}

const getCategoryName = (id) => {
  const cat = categories.value.find(c => c.id === id)
  return cat ? cat.name : 'Nessuna'
}

onMounted(() => {
  fetchCategories()
  fetchProducts()
})
</script>

<style scoped>
    .header-actions { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        margin-bottom: 1rem; 
    }
    .filters { 
        display: flex; 
        gap: 1rem;
        margin-bottom: 1rem; 
        flex-wrap: wrap; 
    }
</style>