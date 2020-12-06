from django.shortcuts import render
from emphasis.models import User
from emphasis.forms import MyNewForm
# Create your views here.

def index(request):
    help_dict = {'help_help' : 'Tired of getting stuck, Mate'}
    return render(request,'help.html',context = help_dict)

def users(request):
    users = User.objects.all()
    user_dict = {'user' : users}
    return render(request,'users.html', context=user_dict)

def login(request):
    form_data = MyNewForm()
    if request.method == 'POST':
        form_data = MyNewForm(request.POST)

        if form_data.is_valid():
            form_data.save(commit = True)
            return index(request)

        else:
            print("INVALID FORM")
    return render(request,'login.html',context = {'form' : form_data})