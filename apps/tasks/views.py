from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Task, Category, SubTask, Comment, TaskLog
from .serializers import (TaskListSerializer, TaskDetailSerializer, CategoryListSerializer,
                          SubTaskSerializer, CommentSerializer)

from common.permissions import IsOwnerOrManagerOrSelf
from .utils import get_tasks_for_user, get_categories_for_user
from apps.notifications.models import Notification
from .services import update_task_status


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
        update_task_status(
            task=self.get_object(),
            user=self.request.user,
            new_status=serializer.validated_data.get("status", self.get_object().status)
        )



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





