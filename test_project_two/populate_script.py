import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_project_two.settings') 

import django
django.setup() 

import random
from emphasis.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    
    
    for user in range(N):
        fake_name = fakegen.name()
        fake_mail = fakegen.email()
        u = User.objects.get_or_create(first_name=fake_name.split(' ')[0],last_name=fake_name.split(' ')[1],email=fake_mail)[0]
    
if __name__ == "__main__":
    print('populating')
    populate(20)
    print('its done!')
