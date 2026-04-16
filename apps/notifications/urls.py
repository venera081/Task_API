from django.urls import path
from . import views 

urlpatterns = [
    path('notifications/', views.NotificationMarkAsReadAPIView.as_view())
]