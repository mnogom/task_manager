from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
<<<<<<< HEAD

from django.shortcuts import render  # noqa: F401
=======
>>>>>>> 03b0126ad80b1189cc5db3712f24e85eb4502c73


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer