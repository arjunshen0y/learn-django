from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Book,Publisher,Author
from .serializers import BookSerializer,PublisherSerializer,AuthorSerializer
# Create your views here.

class BookView(viewsets.ModelViewSet):  #a viewset to view the books data
    #viewsets include all the HTTP requests thus reducing the work of users
    queryset = Book.objects.all()  
    serializer_class = BookSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  #view specific permission class

class PublisherView(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



