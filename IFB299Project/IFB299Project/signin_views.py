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
    return render_to_response('registration/login.html',
                              context_dict, context)


# Defining a function to perform user authentication
# @param username The username submitted in the login form
# @param password The password submitted in the login form
# @param accountNumber The Account Number submitted in the login form
# @returns A boolean based on whether the submitted login credential matches the entries from the database
def authenticate(USERNAME, PASSWORD):
    try:
        if NEWACCOUNT.objects.filter(USERNAME=USERNAME).exists():
            querySet = NEWACCOUNT.objects.get(USERNAME = USERNAME)
            if ((querySet.USERNAME!=USERNAME) or (querySet.PASSWORD != PASSWORD)):
                return False
        else:
            return False
    except ValueError as error:
        return False
    else:
        return True


# Defining a view to display the account balance for a specific user
def signin(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST': # If the form has been submitted
        form = LoginForm(request.POST or None)
        if form.is_valid():                                                     # Checking if the submitted form is valid
            data = form.cleaned_data
            username = data['USERNAME']
            rawPassword = data['PASSWORD']
            password = hashlib.md5(rawPassword.encode('utf-8')).hexdigest()
            isValidUser = authenticate(USERNAME=username, PASSWORD=password)     # Checking if the login credentials are valid
            try:
                if isValidUser:
                    querySet = NEWACCOUNT.objects.get(USERNAME=username)# Obtaining the account detaild matching the submitted ACCOUNTNO
                    querySet.save()
                    context = {

                        "username":username,

                    }
                    s = SessionStore()
                    s.create()
                    return render(request,'smart_city.html',context)


                else:
                    raise ValueError('Incorrect Login Details. Please enter correct entries.')
            except ValueError as error:
                    context = {
                        "form": form,
                        "error_message": error.args[0],
                    }
                    return render(request, 'registration/login.html', context)
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/mainviews/')
