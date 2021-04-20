from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.HyperlinkedModelSerializer): #this serializer hyperlinks primary,foreign keys unlike ModelSerializer
    class Meta:
        model = ToDo
        fields = ('id', 'date', 'tasks',)
