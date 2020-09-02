from django.db import models

# Create your models here.
from django.db import models


class StudentModel(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        db_table = "student"







