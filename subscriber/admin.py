from django.contrib import admin
from .models import Email

# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    list_display = ("id", "signup_email", "created_at")
    list_display_links = ("id", "signup_email")
    search_fields = ("signup_email",)
    list_per_page = 25

admin.site.register(Email, EmailAdmin)