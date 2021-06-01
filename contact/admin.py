from contact.models import Survey
from fourfront_prelaunch.models import Survey
from django.contrib import admin
from .models import Survey

# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "subscriber_first_name", "subscriber_last_name", "subscriber_email", "created_at")
    list_display_links = ("id", "subscriber_first_name")
    search_fields = ("subscriber_first_name", "subscriber_last_name", "subscriber_email")
    list_per_page = 25

admin.site.register(Survey, SurveyAdmin)