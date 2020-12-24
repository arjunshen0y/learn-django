from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookView(viewsets.ModelViewSet):  #a viewset to view the books data
    #viewsets include all the HTTP requests thus reducing the work of users
    queryset = Book.objects.all()  
    serializer_class = BookSerializer



