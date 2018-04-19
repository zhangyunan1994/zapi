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
    path(r'', views.index, name='team/index'),
    path(r'/member', views.index, name="member/index"),
    path(r'/members', views.members, name="member/members"),
    path(r'/members/add', views.add, name="member/add"),
    path(r'/members/modify', views.modify, name="member/modify"),
    path(r'/member/remove', views.remove, name="member/remove"),
    path(r'/departments', views.departments, name="department/list"),
    path(r'/department/add', views.department_add, name="department/add"),
    path(r'/department/delete', views.department_delete, name="department/delete"),
]
