from .models import Notification

def mark_notification_as_read(*, user, notification_id):
    notification = Notification.objects.get(id=notification_id, user=user)
    notification.is_read = True
    notification.save(update_fields=["is_read"])
    return notification