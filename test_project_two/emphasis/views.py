from django.shortcuts import render

# Create your views here.

def index(request):
    help_dict = {'help_help' : 'Tired of getting stuck, Mate'}
    return render(request,'help.html',context = help_dict)
