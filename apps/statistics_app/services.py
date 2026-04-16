from apps.tasks.models import Task

def get_user_statistics(user):
    tasks = Task.objects.filter(owner=user)

    return {
        "total_tasks": tasks.count(),
        "todo": tasks.filter(status="todo").count(),
        "in_progress": tasks.filter(status="in_progress"),
        "done": tasks.filter(status="done").count(),
    }