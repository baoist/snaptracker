from django.forms import ModelForm
from snapshot.models import *

print 'f7u12'

class SnapshotForm(ModelForm):
    class Meta:
        model = Snapshot
