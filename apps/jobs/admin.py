from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "min_salary",
        "max_salary",
    ]

    list_display_links = ["title", "user"]


admin.site.register(Job, JobAdmin)
