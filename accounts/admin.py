"""Admin configuration for accounts app."""

from django.contrib import admin

from .models import User

admin.site.register(User)
