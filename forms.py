from django.forms import ModelForm
from snapshot.models import *

class SnapshotForm(ModelForm):
    class Meta:
        model = Snapshot
