from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Popola il database con dati di esempio'

    def handle(self, *args, **options):
        print('Inizializzazione database di esempio...')

        # -------------
        # Categorie
        # -------------
        electronics, _ = Category.objects.get_or_create(name='Elettronica')
        clothing, _ = Category.objects.get_or_create(name='Abbigliamento')
        books, _ = Category.objects.get_or_create(name='Libri')

        # -------------
        # Prodotti
        # -------------
        products = [
            {
                'name': 'Smartphone',
                'description': 'Un telefono di esempio',
                'price': 299.99,
                'category': electronics,
                'tags': ['telefono', 'elettronica'],
            },
            {
                'name': 'Laptop',
                'description': 'Un computer portatile',
                'price': 899.99,
                'category': electronics,
                'tags': ['computer', 'elettronica'],
            },
            {
                'name': 'Cuffie',
                'description': 'Cuffie wireless',
                'price': 199.99,
                'category': electronics,
                'tags': ['cuffie', 'elettronica'],
            },
            {
                'name': 'T-shirt',
                'description': 'Una maglietta',
                'price': 19.99,
                'category': clothing,
                'tags': ['abbigliamento', 'maglietta'],
            },
            {
                'name': 'Jeans',
                'description': 'Pantaloni di jeans',
                'price': 49.99,
                'category': clothing,
                'tags': ['abbigliamento', 'jeans'],
            },
            {
                'name': 'Giacca',
                'description': 'Una giacca invernale',
                'price': 89.99,
                'category': clothing,
                'tags': ['abbigliamento', 'giacca'],
            },
            {
                'name': 'Libro di programmazione',
                'description': 'Un libro su Python',
                'price': 39.99,
                'category': books,
                'tags': ['libro', 'programmazione'],
            },
            {
                'name': 'Libro di cucina',
                'description': 'Ricette senza glutine',
                'price': 24.99,
                'category': books,
                'tags': ['libro', 'cucina'],
            },
        ]

        created_count = 0

        for product_data in products:
            obj, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1

        print(f'Database inizializzato! {created_count} prodotti creati.')
