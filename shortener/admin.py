from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ["id", "original_url", "short_path", "clicks", "created_at"]
