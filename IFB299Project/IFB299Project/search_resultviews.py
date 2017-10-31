from django.http import *
from django.views.generic.base import *
#from django.contrib.staticfiles import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from IFB299Project.models import Placeinformation
from IFB299Project.models import NEWACCOUNT
from IFB299Project.signin_views import signin


def index(request, *args, **kwargs):
    placelist = Placeinformation.objects.all()
    context_dict = {'Places': placelist}
    return render_to_response('search_result_page.html',
                              context_dict)

def show_resulttt(request):
    context = RequestContext(signin(request))
    context_dict = {}

    try:
        user = request.GET.get('username1')
        userinfo = NEWACCOUNT.objects.get(USERNAME=user)
        usertype=userinfo.TYPE
        query = request.GET.get('q')
        resultwithquery = Placeinformation.objects.filter(Placename__contains=query)
        result = resultwithquery.filter(typeOfPlace__contains=usertype)
        context_dict = {'result': result}
    except Placeinformation.DoesNotExist:

        context_dict['result'] = None
    # Go render the response and return it to the client.
    return render_to_response('search_result_page.html', context_dict,context)