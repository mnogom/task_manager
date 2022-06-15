from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer