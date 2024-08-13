from rest_framework import serializers


class TasksSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()
    