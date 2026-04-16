from rest_framework import serializers
from .models import Task, Category, SubTask, Comment, TaskLog

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

class SubTaskSerializer(serializers.ModelSerializer):
   class Meta:
      model = SubTask
      fields = '__all__'
      
class CommentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Comment
      fields = '__all__'
      read_only_fields = ['author']