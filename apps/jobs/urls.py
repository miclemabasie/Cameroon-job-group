from django.urls import path
from .views import list_view, job_create_view

app_name = "jobs"

urlpatterns = [
    path("", list_view, name="list_jobs"),
    path("create/", job_create_view, name="create_job"),
]
