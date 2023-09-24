from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from neural_admin.admin import CustomAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(CustomAdmin, UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email", "card_number", "pin_code")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "id",
        "first_name",
        "last_name",
        "date_of_birth",
        "card_number",
    )
    email_fields = ("email",)
    blur_fields = ("pin_code",)
    list_display_links = ("id", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "sold_products")

    @admin.display(description="Date of birth")
    def date_of_birth(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")
