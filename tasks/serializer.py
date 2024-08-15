from rest_framework import serializers
from .models import Tasks


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('body', )