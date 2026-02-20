from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Task, Category, SubTask, Comment, TaskLog
from .serializers import (TaskListSerializer, TaskDetailSerializer, CategoryListSerializer,
                          SubTaskSerializer, CommentSerializer)

from common.permissions import IsOwnerOrManagerOrSelf
from .utils import get_tasks_for_user, get_categories_for_user
from notifications.models import Notification


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrSelf]
    filterset_fields = ['status', 'priority', 'category']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'deadline']

    def get_queryset(self):
        return get_tasks_for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrSelf]

    def get_queryset(self):
        return get_tasks_for_user(self.request.user)
    
    def perform_update(self, serializer):
        old_status = self.get_object().status
        instance = serializer.save()

        if old_status != instance.status:
            TaskLog.objects.create(
                task=instance,
               changed_by=self.request.user,
               old_status=old_status,
               new_status=instance.status
            )

            Notification.objects.create(
                user=instance.owner,
                message=f"Your task '{instance.title}' status changed to {instance.status}")
            




class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrSelf]

    def get_queryset(self):
        return get_categories_for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubTaskListCreateAPIView(ListCreateAPIView):
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SubTask.objects.filter(task__owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save()


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(task__owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





