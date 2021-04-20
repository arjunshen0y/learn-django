from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer