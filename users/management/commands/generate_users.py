from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

faker = Faker()


class Command(BaseCommand):
    help = "Creates users objects"

    def add_arguments(self, parser):
        parser.add_argument(
            "users_count",
            type=int,
            nargs="?",
            default=100,
            help="Indicates the number of users to be created",
        )

    def handle(self, *args, **kwargs):
        users_count = kwargs.get("users_count")
        User = get_user_model()

        for _ in range(users_count):
            profile = faker.simple_profile()
            user = User(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                username=profile["username"],
                email=profile["mail"],
                card_number=faker.credit_card_number(),
                pin_code=faker.credit_card_security_code(),
            )
            user.set_password("password")
            user.save()
