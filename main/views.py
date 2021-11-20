from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer

from .models import Task
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view tasks
    """
    queryset = Task.objects.all().order_by('-created')
    serializer_class = TaskSerializer

#permission_classes = [permissions.IsAuthenticated]