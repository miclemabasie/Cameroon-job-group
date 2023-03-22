from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("superadmin/", admin.site.urls),
    path("jobs/", include("apps.jobs.urls", namespace="jobs")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Cameron Job Group Admin"
admin.site.site_title = "Camerroon Job Group Admin Portal"
admin.site.index_title = "Welcom to the CM Job Group Portal"
