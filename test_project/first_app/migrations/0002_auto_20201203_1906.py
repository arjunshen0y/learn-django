# Generated by Django 3.1.3 on 2020-12-03 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Acess_Record',
            new_name='Access_Record',
        ),
        migrations.RenameField(
            model_name='webpage',
            old_name='Topic',
            new_name='topic',
        ),
    ]
