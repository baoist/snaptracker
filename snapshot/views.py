# Create your views here.
from django import template, http, forms
from snapshot.models import *
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import datetime

def snap(request):
    if request.method == 'POST':
        form = PlannedForm(request.POST)
        if form.is_valid():
            print form
            return HttpResponseRedirect('/snapshot/complete/')
    else:
        form = PlannedForm()
    
    return render_to_response('snapshot/snap.html', {
                                'images': 'foo', 
                                'formset': form.as_p, 
                                'current_date': datetime.datetime.now().strftime('%Y/%m/%d'), 
                            },
                            context_instance = template.RequestContext(request))

def complete(request):
    return render_to_response('snapshot/complete.html', {}, context_instance = template.RequestContext(request))

def home(request):
    return render_to_response('snapshot/home.html', {}, context_instance = template.RequestContext(request))
