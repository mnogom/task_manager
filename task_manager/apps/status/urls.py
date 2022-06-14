"""Urls."""

from django.urls import path

from .views import (ListCreateStatusView,
                    RetrieveUpdateDestroyStatusView)


app_name = 'status'
urlpatterns = [
    path('', ListCreateStatusView.as_view(), name='list'),
    path('<int:pk>/', RetrieveUpdateDestroyStatusView.as_view(), name='sample'),
]
