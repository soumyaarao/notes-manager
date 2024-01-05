from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from users.models import CustomUser
from users.serializers import UserSerializer


@api_view(['POST'])
def user_registration(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not password or not password:
        return Response({'message': 'Invalid username/password format'}, status=status.HTTP_400_BAD_REQUEST)
    user = CustomUser(username=username)
    user.set_password(password)
    user.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username)
    if not user:
        return Response({'message': 'Username invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    user = user[0]
    if user.log_in(password):
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
