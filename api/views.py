from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'console/api/index.html')


def team(request):
    return render(request, 'console/api/member.html')