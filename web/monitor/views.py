from django.shortcuts import render
from .models import Monitor
from rest_framework import viewsets
from .serializers import MonitorSerializers

# Create your views here.
def index(requests):
  monitors = Monitor.objects.all().order_by("-created_at")
  return render(requests, "index.html", {"monitors": monitors})

class MonitorViewSet(viewsets.ModelViewSet):
  queryset = Monitor.objects.all()
  serializer_class = MonitorSerializers
