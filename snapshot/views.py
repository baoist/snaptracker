from django import db, template, http, forms
from snapshot.models import *
from django.db import models
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import datetime

def estimate_leave(current):
    estimated_out = int(current) + 5
    if estimated_out > 12:
        estimated_out -= 12
    return estimated_out

def snap(request):
    if request.method == 'POST':
        snap_form = PlannedForm(request.POST)
        project_form = ProjectForm(request.POST)
        if snap_form.is_valid() and project_form.is_valid():
            snap_form.save()
            project_form.save(commit=False) # linked to snap_form
            return HttpResponseRedirect('/snapshot/complete/')
    else:
        current_hour = datetime.datetime.now().strftime('%l')
        snap_form = PlannedForm(initial={
                            'start': current_hour,
                            'end': estimate_leave(current_hour),
                        })
        project_form = ProjectForm()
    return render_to_response('snapshot/snap.html', {
                                'images': 'foo',
                                'snap_formset': snap_form.as_p,
                                'project_formset': project_form.as_p,
                                'current_date': datetime.datetime.now().strftime('%Y/%m/%d'),
                            },
                            context_instance = template.RequestContext(request))

def complete(request):
    return render_to_response('snapshot/complete.html', {}, context_instance = template.RequestContext(request))

def listall(request):
    all_snaps = Planned.objects.all()
    return render_to_response('snapshot/list.html', {
                                'snaps': all_snaps,
                            }, 
                            context_instance = template.RequestContext(request))

def home(request):
    return render_to_response('snapshot/home.html', {}, context_instance = template.RequestContext(request))
