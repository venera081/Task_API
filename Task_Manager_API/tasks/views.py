from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Task, Category
from .serializers import TaskListSerializer, TaskDetailSerializer, CategoryListSerializer
from common.permissions import IsOwnerOrManagerOrSelf
from .utils import get_tasks_for_user, get_categories_for_user



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



class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrSelf]

    def get_queryset(self):
        return get_categories_for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
