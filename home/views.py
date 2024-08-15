from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TasksSerializer
from tasks.models import Tasks
from rest_framework import status


# Create your views here.
class HomeView(APIView):
    def get(self, request):
        #tasks = Tasks.objects.filter(user=request.user.id)
        tasks = Tasks.objects.all()
        ser_data = TasksSerializer(instance=tasks, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)