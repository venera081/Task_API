from rest_framework import serializers

class UserStatisticsSerializer(serializers.Serializer):
    total_tasks = serializers.IntegerField()
    todo = serializers.IntegerField()
    in_progress = serializers.IntegerField()
    done = serializers.IntegerField()