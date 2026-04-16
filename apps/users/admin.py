from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "is_active")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "is_active")}),
        ("Important dates", {"fields": ("last_login",)}),
    )