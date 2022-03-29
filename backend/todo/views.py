from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework import viewsets
from .models import Todo
from rest_framework_swagger.views import get_swagger_view

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    """
    retrieve:
        List all the users.
        
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
