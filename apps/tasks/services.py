from .models import Task, TaskLog
from apps.notifications.models import Notification


def update_task_status(*, task, user, new_status):
    old_status = task.status

    task.status = new_status
    task.save(update_fields=["status"])

    if old_status != new_status:
        TaskLog.objects.create(
            task=task,
            changed_by=user,
            old_status=old_status,
            new_status=new_status
        )

        Notification.objects.create(
            user=task.owner,
            message=f"Your task '{task.title}' status changed to {new_status}"
        )

    return task