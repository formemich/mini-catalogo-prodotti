# Mini Catalogo Prodotti Full-Stack

Progetto per colloquio tecnico: gestione catalogo prodotti con categorie, filtri avanzati e paginazione.

## Tecnologie Utilizzate
- **Backend**: Django 5 + Django REST Framework
- **Frontend**: Vue 3 (Vite) + PrimeVue (Aura Theme)
- **Database**: PostgreSQL
- **DevOps**: Docker & Docker Compose

## Installazione (Docker)
Il modo più veloce per avviare il progetto è tramite Docker.

1. Clona la repository:
   ```bash
   git clone <url-tua-repo>
   cd mini-catalogo
   ```

2. Avvia i container:
   ```bash
   docker-compose up --build
   ```

3. Inizializza il db (Facoltativo):
   ```bash
   docker-compose exec web python manage.py init_db
   ```

# Funzionalità Implementate
- CRUD Prodotti e Categorie
- Filtri lato server: Ricerca testuale, Categoria, Prezzo Min/Max
- Paginazione e Ordinamento gestiti dal backend
- Gestione errori con notifiche Toast e modali di conferma
- Dark/Light Mode toggle per UX

## Test Automatici

Il progetto include una suite di test per il Backend per garantire la correttezza della logica di business, delle validazioni e dei filtri API.

### Eseguire i test (Docker)
```bash
docker-compose exec backend python manage.py test
```
