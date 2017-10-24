from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from IFB299Project.models import Placeinformation

def index(request, *args, **kwargs):
    context = RequestContext(request)
    placelist = Placeinformation.Placename
    context_dict = {'places':placelist}
    return render_to_response('smart_city.html',
                              context_dict)