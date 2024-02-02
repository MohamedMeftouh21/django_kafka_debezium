from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from base.serializers import UserRegisterSerializer
from rest_framework.decorators import api_view

from base.models import CustomUser

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		serializer = UserRegisterSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(serializer.validated_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET'])
def getUser(request):
    user = CustomUser.objects.all()
    serializer = UserRegisterSerializer(user, many=True)
    return Response(serializer.data)