# Generated by Django 3.0.5 on 2020-09-02 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listsse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='text',
        ),
    ]
