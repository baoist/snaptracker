# Create your views here.
from django import template, http, forms
from snapshot.models import *
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import datetime

PROJECTS_AVAILABLE = (
    (u'test1', u'test1'),
    (u'2', u'test2'),
    (u'3', u'test3'),
    (u'4', u'test4'),
    (u'5', u'test5'),
)

def snap(request):
    if request.method == 'POST':
        snap_form = PlannedForm(request.POST)
        project_form = ProjectForm(request.POST)
        if snap_form.is_valid() and project_form.is_valid():
            return HttpResponseRedirect('/snapshot/complete/')
    else:
        snap_form = PlannedForm({
                            'start': datetime.datetime.now().strftime('%l'),
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

def home(request):
    return render_to_response('snapshot/home.html', {}, context_instance = template.RequestContext(request))
