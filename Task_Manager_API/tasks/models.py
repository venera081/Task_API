from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=55, choices=[
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], default='todo')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    priority = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        default='medium'
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)


class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    changed_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    old_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    changed_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
