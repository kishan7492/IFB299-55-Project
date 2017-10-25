"""IFB299Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from IFB299Project import mainviews
from IFB299Project import signup_views
from IFB299Project import signin_views
from IFB299Project import resultviews
from IFB299Project import search_resultviews
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static

from IFB299Project import signup_views as signup_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mainviews', mainviews.index, name='mainpage'),
    url(r'^$', mainviews.index, name='mainpage'),
    url(r'^signup/$', signup_views.signup, name='signup'),



    url(r'^signin', signin_views.index, name='signin'),
    url(r'^search_result', search_resultviews.index, name='searchresult'),
    #url(r'^result', resultviews.index, name='result'),
    url(r'^show_result/(?P<ID>[1-9]+)$',resultviews.show_result, name='show_result'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
