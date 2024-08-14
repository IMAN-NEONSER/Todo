from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import UserRegisterSerializer


# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data)
        return Response(ser_data.errors)