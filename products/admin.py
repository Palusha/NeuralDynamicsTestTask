from typing import Any
from django.contrib import admin, messages
from django.db.models import Count, Sum
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "price",
        "_description",
        "owner",
        "created_at",
    )
    list_display_links = ("id", "name", "slug")
    filter_horizontal = ("customers",)
    exclude = ("slug",)

    def _description(self, obj):
        return mark_safe(obj.description)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        query = self.model.objects.filter(owner=request.user).aggregate(
            total_count=Count("id"), total_sum=Sum("price")
        )
        messages.add_message(
            request,
            messages.INFO,
            f"Your products count {query['total_count']}.\n Overall sum: {query['total_sum']}",
        )


admin.site.register(Product, ProductAdmin)
