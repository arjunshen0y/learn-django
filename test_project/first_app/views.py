from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,Access_Record

# Create your views here.
def index(request):
    webpage_list = Access_Record.objects.order_by('date')  # here order_by returns a queryset(list of tuples) and stored in a list
    date_dict = {'access_record' : webpage_list}
    return render(request,'index.html',context = date_dict)


