from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from project.models import Project


def index(request):
    return render(request, 'console/project/index.html')


def project_list(request):
    project_name = request.GET.get('project_name')
    result = Project.objects
    if project_name:
        result = result.filter(name__icontains=project_name)
    result = result.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def add(request):
    name = request.POST.get("name")
    remark = request.POST.get("remark")
    department_id = request.POST.get("department_id")
    version = request.POST.get("version")
    Project.objects.create(name=name, version=version, remark=remark, department_id=department_id, status=0)
    return JsonResponse({"code": 200}, safe=False)
