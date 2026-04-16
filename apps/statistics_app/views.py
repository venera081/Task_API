from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserStatisticsSerializer
from apps.statistics_app.services import get_user_statistics

class UserStatisticsAPIView(GenericAPIView):
    serializer_class = UserStatisticsSerializer

    def get(self, request):
        data = get_user_statistics(request.user)
        serializer = self.get_serializer(data)
        return Response(serializer.data)