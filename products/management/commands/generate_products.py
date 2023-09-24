import random

import faker_commerce
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from products.models import Product

faker = Faker()
faker.add_provider(faker_commerce.Provider)


class Command(BaseCommand):
    help = "Creates products objects"

    def add_arguments(self, parser):
        parser.add_argument(
            "products_count",
            type=int,
            nargs="?",
            default=100,
            help="Indicates the number of products to be created",
        )

    def handle(self, *args, **kwargs):
        products_count = kwargs.get("products_count")
        User = get_user_model()
        users_id = User.objects.values_list("id", flat=True)

        for _ in range(products_count):
            product = Product.objects.create(
                name=faker.ecommerce_name(),
                price=faker.pyfloat(right_digits=2, positive=True, max_value=100000),
                description=faker.paragraph(
                    nb_sentences=20, variable_nb_sentences=True
                ),
                owner_id=random.choice(users_id),
            )
            product.customers.add(*random.choices(users_id, k=random.randint(5, 40)))
