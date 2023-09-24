from creditcards.models import CardNumberField, SecurityCodeField

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    card_number = CardNumberField()
    pin_code = SecurityCodeField()
