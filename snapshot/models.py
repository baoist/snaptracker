from django.db import models
from django.forms import ModelForm
import datetime

PROJECTS_AVAILABLE = (
    (u'', u'Add Project'),
    (u'1', u'test1'),
    (u'2', u'test2'),
    (u'3', u'test3'),
    (u'4', u'test4'),
    (u'5', u'test5'),
)

# Create your models here.
class Planned(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    date = models.DateTimeField('date published')

class Actual(models.Model):
    planned = models.ForeignKey(Planned, primary_key=True)
    hours = models.IntegerField()
    accomplished = models.CharField(max_length=223)
    date = models.DateTimeField('date published')

class Project(models.Model):
    planned = models.ForeignKey(Planned, primary_key=True)
    name = models.CharField(max_length=223, choices=PROJECTS_AVAILABLE, default='-') 
    expected_end = models.DateTimeField(auto_now=False)
    date = models.DateTimeField('date published')

class Task(models.Model):
    planned = models.ForeignKey(Planned, primary_key=True)
    name = models.CharField(max_length=223)

class PlannedForm(ModelForm):
    class Meta:
        model = Planned
        exclude = ('date',)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('planned', 'expected_end', 'date',)

class ActualForm(ModelForm):
    class Meta:
        model = Actual
        exclude = ('date',)
