from django.db import models

# Create your models here.
class Planned(models.Model):
  start = models.IntegerField()
  end = models.IntegerField()
  date = models.DateTimeField('date published')

class Actual(models.Model):
  planned = models.ForeignKey(Planned)
  hours = models.IntegerField()
  accomplished = models.CharField(max_length=223)
  date = models.DateTimeField('date published')

class Project(models.Model):
  planned = models.ForeignKey(Planned)
  name = models.CharField(max_length=223) 
  expected_end = models.DateTimeField(auto_now=False)
  date = models.DateTimeField('date published')

class Task(models.Model):
  planned = models.ForeignKey(Planned)
  name = models.CharField(max_length=223)
