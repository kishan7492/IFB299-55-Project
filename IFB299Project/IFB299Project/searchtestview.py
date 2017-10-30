import operator

from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from models import Placeinformation
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView

#class searchdb(queryyy):
        #BlogSearchListView
"""
Display a Blog List page filtered by the search query.
"""
#paginate_by = 10




placelist = ListView.as_view(
  queryset=Placeinformation.objects.all(),
)

def get_queryset(query):
        #result = super(searchdb, self).get_queryset()
        context_dict = {}
        result = ''
        keywords = query.request.GET.get('q')
        if keywords:
            query_list = keywords.split()
            query = SearchQuery(keywords)
            vector = SearchVector('Placename')
            result = result.annotate(search=vector).filter(search=query)
            context_dict['result'] = result
        return render_to_response('search_result_page.html', context_dict)