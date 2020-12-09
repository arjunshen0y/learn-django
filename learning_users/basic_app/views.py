from django.shortcuts import render
from .forms import UserForm,UserExtra

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    
    registered = False                  # first we assume that the user has not registered

    if request.method == 'POST':
        user_form = UserForm(request.POST)  #   # these two variables are instances of the model forms while request is post
        profile_form = UserExtra(request.POST)

        if user_form.is_valid() and profile_form.is_valid():        #checks wheather the two forms are valid

            user = user_form.save()             #saves the data from the form
            user.set_password(user.password)    #sets the password , also hashing is undergone
            user.save()                         #saves data and pswd

            profile = profile_form.save(commit=False)  #we need to check wheather profile pic is present, so data is not added to the db
            profile.user = user  #defines the one to one relation of user that is shown in models

            if 'profile_pic' in request.FILES: #
                profile.profile_pic = request.FILES['profile_pic']  #if we included pro pic we assign it to the db and request.FILES is actually a dict of all the files added to form

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors) #shows error if form is invalid
    
    else:
         user_form = UserForm()
         profile_form = UserExtra()

    return render(request, 'basic_app/registration.html',context={'user_form':user_form , 'profile_form' :profile_form, 'registered':registered})

   


