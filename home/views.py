from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TasksSerializer
from tasks.models import Task
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #tasks = Tasks.objects.filter(user=request.user.id)
        tasks = Task.objects.all()
        ser_data = TasksSerializer(instance=tasks, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)