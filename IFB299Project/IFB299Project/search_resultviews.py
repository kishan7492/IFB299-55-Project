from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from IFB299Project.models import Placeinformation


def index(request, *args, **kwargs):
    placelist = Placeinformation.objects.all()
    context_dict = {'Places': placelist}
    return render_to_response('search_result_page.html',
                              context_dict)
