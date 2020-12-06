from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'sample_app/index.html')

def form_name_view(request):
    form_data = forms.FormName()
    
    
    if request.method == 'POST':
        form_data = forms.FormName(request.POST)

        if form_data.is_valid():
            print('name is :' + form_data.cleaned_data['name'])
            print('email is :' + form_data.cleaned_data['email'])
            print('text is :' + form_data.cleaned_data['text'])

    return render(request, 'sample_app/forms.html',context={'form' : form_data})