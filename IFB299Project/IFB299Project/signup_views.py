from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from IFB299Project.forms import SignUpForm

def index(request, *args, **kwargs):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('signup.html',
                              context_dict, context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})