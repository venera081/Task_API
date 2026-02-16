from rest_framework import serializers
from .models import Task, Category

class CategoryListSerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = 'id name owner created_at'.split()
      read_only_fields = ['owner']

class TaskListSerializer(serializers.ModelSerializer):
   class Meta:
      model = Task
      fields = 'id title status owner category created_at'.split()
      read_only_fields = ['owner']

class TaskDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = Task
      fields = '__all__'
      read_only_fields = ['owner']      