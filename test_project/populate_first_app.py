import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_project.settings')       #links this py file to the settings file of the project

import django
django.setup()    #sets up django


#fake population script
import random
from first_app.models import Webpage,Topic,Access_Record
from faker import Faker

fako = Faker()
#random topics manual list
topic = ['Social Media','Shopping','Game','News','Education']


#creating a function for Topic . adding to Topic table via created list as topics cannot be randomly generted through faker
def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topic))[0] #---> first element of the tuple is stored in variable 't', the tuple is (value,boolean)
    t.save()
    return t


#populate function

def populate(N=5): 
    for entry in range(N):
        top = add_topic()

        #creating fake data
        fake_name = fako.company()
        fake_date = fako.date()
        fake_url = fako.url()

        #adding to Webpage table
        wb = Webpage.objects.get_or_create(topic=top, name = fake_name, url = fake_url)[0]
     
        #adding to Access_Record
        ar = Access_Record.objects.get_or_create(name= wb, date=fake_date)[0]

#main function

if __name__ == 'main':
    print('populating')
    populate(10)
    print('done')


