"""Views."""

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Status
from .serializers import StatusSerializer


class ListCreateStatusView(ListCreateAPIView):
    queryset = Status.objects.order_by('name')
    serializer_class = StatusSerializer


class RetrieveUpdateDestroyStatusView(RetrieveUpdateDestroyAPIView):
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
