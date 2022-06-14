"""Urls."""

from django.urls import path

from .views import (ListCreateLabelView,
                    RetrieveUpdateDestroyLabelView)


app_name = 'label'
urlpatterns = [
    path('', ListCreateLabelView.as_view(), name='list'),
    path('<int:pk>/', RetrieveUpdateDestroyLabelView.as_view(), name='sample'),
]
