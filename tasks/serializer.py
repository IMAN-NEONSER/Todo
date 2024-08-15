from rest_framework import serializers
from .models import Tasks


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('body', )

    def create(self, validated_data):
        return Tasks.objects.create(**validated_data)