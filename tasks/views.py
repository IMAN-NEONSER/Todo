from .serializer import AddTaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tasks
from rest_framework import status


# Create your views here.
class AddTaskView(APIView):
    def post(self, request):
        ser_data = AddTaskSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDoneView(APIView):
    def delete(self, request, task_id, format=None):
        try:
            task = Tasks.objects.get(id=task_id)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)