from django.contrib import admin
from django.urls import path, include
from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/tasks/', include('apps.tasks.urls')),
    path('api/v1/company/', include('apps.company.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/statistics_app/', include('apps.statistics_app.urls')),


]

urlpatterns += yasg.urlpatterns