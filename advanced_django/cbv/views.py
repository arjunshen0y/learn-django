from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

# Create your views here.

class Index(TemplateView):

    template_name = 'cbv/index.html'

    def get_context_data(self,**kwargs):    #for passing the context dictionary
        
        context = super().get_context_data(**kwargs)
        context['key_injection'] = "Welcome to CBV"
        return context

class SampleList(ListView):
    model = models.Student   #an object called student_list is created and send as context dictionary
    template_name = 'cbv/'


class SampleDetail(DetailView):
    model = models.Student
    #default context dictionary name is school, we change it to student_details in the next line
    context_object_name = 'student_details'

    
    


