from rest_framework.generics import ListAPIView, UpdateAPIView
from .serializers import NotificationSerializer
from .models import Notification
from rest_framework.permissions import IsAuthenticated


class NotificationMarkAsReadAPIView(UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        from .services import mark_notification_as_read

        mark_notification_as_read(
            user=self.request.user,
            notification_id=self.get_object().id
        )