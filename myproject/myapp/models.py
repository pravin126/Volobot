from django.db import models

# myapp/models.py
from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=255)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
