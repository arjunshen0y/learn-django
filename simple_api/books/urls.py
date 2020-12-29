from django.urls import path,include
from . import views
from rest_framework import routers  #generates all url

#app_name = 'books'

router = routers.DefaultRouter() #router is an instance of DefaultRouter 
router.register('books', views.BookView)
router.register('publisherss', views.PublisherView)
router.register('authors', views.AuthorView)

urlpatterns = [
   path('',include(router.urls))
]