from rest_framework.generics import ListCreateAPIView
from .serializers import CompanySerializer
from .models import Company
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOwnerRole

class CompanyListCreateAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsOwnerRole]

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        from .services import create_company

        instance = create_company(
            user=self.request.user,
            **serializer.validated_data
        )
        serializer.instance = instance