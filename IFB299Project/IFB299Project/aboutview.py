from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import NEWACCOUNT
from forms import LoginForm
import hashlib
from django.shortcuts import render
from django.contrib.auth.views import logout
from django.contrib.sessions.backends.db import SessionStore

def index(request, *args, **kwargs):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('about.html',
                              context_dict, context)
