from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
import hashlib
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from models import NEWACCOUNT
from forms import CreateAccount


def index(request, *args, **kwargs):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('signup.html',
                              context_dict, context)


def signup(request):
    form = CreateAccount(request.POST or None)
    if request.method == 'POST':
        form = CreateAccount(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            username = data['USERNAME']  # Obtaining data from the submitted form
            rawPassword = data['PASSWORD']
            password = hashlib.md5(rawPassword.encode('utf-8')).hexdigest()  # Hashing the user password
            confirmPass = data['REPASSWORD']
            address = data['ADDRESS']
            firstname = data['FIRSTNAME']
            lastname = data['LASTNAME']
            email = data['EMAIL']
            try:
                if rawPassword != confirmPass:
                    raise ValueError('Passwords do not match. Please ensure password and confirm password are the same!')
            except ValueError as error:
                context = {
                    "form": form,
                    "error_message": error.args[0],
                }
                return render(request, 'signup.html', context)
            else:
                new_user = NEWACCOUNT(USERNAME=username, FIRSTNAME=firstname,LASTNAME=lastname,EMAIL=email, PASSWORD=password, ADDRESS=address, TYPE=type, )
                new_user.save()
                context={
                    "username" : username
                }
                return render(request, 'smart_city.html',context)

    context = {
        "form": form,
    }
    return render(request,'signup.html',context)


#form = CreateAccount(request.POST or None)
#    if request.method == 'POST':
 #       form = CreateAccount(request.POST or None)
  #      if form.is_valid():
   #         data = form.cleaned_data  # Cleaning any corrupt form data
    #        username = data['USERNAME']  # Obtaining data from the submitted form
     #       rawPassword = data['PASSWORD']
      #      password = hashlib.md5(rawPassword.encode('utf-8')).hexdigest()  # Hashing the user password
       #     confirmPass = data['REPASSWORD']
        #    address = data['ADDRESS']
#            type = data['TYPE']
#
 #           try:  # Performing backend form validation for any invalid data
  #              if rawPassword != confirmPass:
   #                 raise ValueError(
    #                    'Passwords do not match. Please ensure password and confirm password are the same!')
     #       except ValueError as error:  # Raising an exception in case of invalid data
      #          context = {
       #             "form": form,
        #            "error_message": error.args[0],
         #       }
          #      return render(request,'signup.html', context)
#
 #           else:  # Saving the data in the database
  #              new_user = NEWACCOUNT(USERNAME=username, PASSWORD=password, REPASSWORD=password,
   #                                    ADDRESS=address, TYPE=type,
    #                                  )
     #           new_user.save()
#
 #               return render(request,'registration/login.html')
#