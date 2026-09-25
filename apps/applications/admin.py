from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "start_date", "payment", "status", "created_at")
    list_editable = ("status",)
    list_filter = ("status", "course")
    search_fields = ("user__username", "course")