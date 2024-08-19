from rest_framework import serializers
from .models import Task


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('body', )

    def create(self, validated_data):
        return Task.objects.create(**validated_data)