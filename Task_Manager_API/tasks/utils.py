from .models import Task, Category


def get_tasks_for_user(user):
    if user.role == 'owner':
        return Task.objects.all()
    if user.role == 'manager':
        return Task.objects.filter(owner__role='employee')

    return Task.objects.filter(owner=user)


def get_categories_for_user(user):
    
    if user.role == 'owner':
        return Category.objects.all()
    if user.role == 'manager':
        return Category.objects.filter(owner__role='employee')

    return Category.objects.filter(owner=user)
