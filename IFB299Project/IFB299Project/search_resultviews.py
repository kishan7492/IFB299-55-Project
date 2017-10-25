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
def show_resulttt(request, queryyy):

    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        #keywords = self.request.GET.get(queryyy)
        result = Placeinformation.objects.get(Placename=queryyy)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        ###pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict = {'result': result}
        # We also add the category object from
        # the database to thcontext dictionary.
        # We'll use this in the template to verify that the category exists. context_dict['category'] = category
    except Placeinformation.DoesNotExist:

        context_dict['result'] = None
    # Go render the response and return it to the client.
    context = RequestContext(request)

    return render_to_response('search_result_page.html', context_dict, context)