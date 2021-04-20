from django.test import TestCase
from .models import ToDo
from datetime import date
# Create your tests here.

class ToDoModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        today = date.today()
        ToDo.objects.create(date=today.strftime("%Y/%m/%d"), tasks ='learn fast')

    def test_date_content(self):

        todo = ToDo.objects.get(id=1)
        expected_object_name = f'{todo.date}'
        self.assertEquals(expected_object_name, '2021-04-20')

    def test_tasks_content(self):

        todo = ToDo.objects.get(id=1)
        expected_object_name = f'{todo.tasks}'
        self.assertEquals(expected_object_name, 'learn fast')
