from django.db import models
from django.forms import ModelForm
from models import Snapshot, Actual, Project, Task

print 'f7u12'

class SnapshotForm(ModelForm):
    class Meta:
        model = Snapshot

