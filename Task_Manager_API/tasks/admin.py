from django.contrib import admin
from .models import Category, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'owner', 'category')
    list_filter = ('status', 'category')

admin.site.register(Category)