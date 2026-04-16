from django.urls import path
from .views import UserStatisticsAPIView

urlpatterns = [
    path("stats/", UserStatisticsAPIView.as_view())
]