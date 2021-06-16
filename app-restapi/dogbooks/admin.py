from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Dogbook, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Dogbook)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "field",
        "year",
        "created_date",
        "updated_date",
    )
    list_display = (
        "title",
        "field",
        "year",
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )
