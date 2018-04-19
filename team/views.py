from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from team.models import Member, Department

__author__ = 'yunan.zhang zyndev@gmail.com'


def index(request):
    return render(request, "console/member/index.html")

# Create your views here.

def members(request):
    """
    Search members by name or telephone.
    Todo: 此处需要添加公司限制
    :param request:
    :return:
    """
    search_param = request.GET.get("searchParam", None)
    if not search_param:
        result = Member.objects.values().all()
    else:
        result = Member.objects.filter(name__icontains=search_param).values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def add(request):
    """
    add a member.
    TODO: 此处需要添加公司限制和给予登录权限
    :param request:
    :return:
    """
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    department_id = request.POST.get("department_id")
    Member.objects.create(name=name, email=email, phone=phone, department_id=department_id)
    return JsonResponse({"code": 200}, safe=False)


def modify(request):
    """
    modify member's info.
    :param request:
    :return:
    """
    id = request.POST.get("id")
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    Member.objects.filter(id=id).update(name=name, email=email, phone=phone)
    return JsonResponse({"code": 200}, safe=False)


def remove(request):
    """
    remove a member.
    :param request:
    :return:
    """
    id = request.POST.get("id")
    Member.objects.filter(id=id).delete()
    return JsonResponse({"code": 200}, safe=False)


def departments(request):
    result = Department.objects.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def department_add(request):
    name = request.POST.get("department_name")
    Department.objects.create(name=name)
    return JsonResponse({"code": 200}, safe=False)


def department_delete(request):
    id = request.POST.get("id")
    Department.objects.filter(id=id).delete()
    return JsonResponse({"code": 200}, safe=False)