from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TasksSerializer
from tasks.models import Tasks

# Create your views here.


class HomeView(APIView):
    def get(self, request):
        tasks = Tasks.objects.filter(user=request.user)
        ser_data = TasksSerializer(instance=tasks, many=True)
        return Response(data=ser_data.data)