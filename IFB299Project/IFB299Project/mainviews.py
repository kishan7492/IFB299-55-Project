from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from IFB299Project.models import Placeinformation
from IFB299Project.models import Category

from IFB299Project.signin_views import signin
def index(request, *args, **kwargs):
    context = RequestContext(signin(request))
    context_dict = {'a':"js"}

    return render_to_response('smart_city.html',
                              context_dict,context)