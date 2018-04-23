"""zapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='api/index'),
    path(r'team', views.team, name='api/team'),
    path(r'list', views.api_list, name='api/list'),
    path(r'add', views.api_add, name='api/add'),
    path(r'adda', views.api_add_api, name='api/adda'),
    path(r'search', views.api_search, name='api/search'),
    path(r'edit', views.edit, name='api/edit'),
    path(r'get', views.api_get, name='api/get'),
    path(r'detail', views.api_detail, name='api/detail'),
    path(r'update', views.api_update, name='api/update'),
    path(r'delete', views.api_delete, name='api/delete'),
    path(r'environment', views.api_environment, name='api/environment'),
    path(r'environment/add', views.api_environment_add, name='api/environment/add'),
    path(r'environment/list', views.api_environment_list, name='api/environment/list'),
]
