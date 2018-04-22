import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Api


def index(request):
    return render(request, 'console/api/index.html')


def team(request):
    return render(request, 'console/api/member.html')


def api_list(request):
    return render(request, 'console/api/list.html')


def api_add(request):
    return render(request, 'console/api/add.html')


def edit(request):
    return render(request, 'console/api/edit.html')


def api_detail(request):
    return render(request, 'console/api/detail.html')


def api_add_api(request):
    req = json.loads(request.body)
    Api.objects.create(name=req['api_param']['name'], http=req['api_param']['http'], method=req['api_param']['method'],
                       url=req['api_param']['url'],
                       request_params=json.dumps(req['request_params']),
                       response_params=json.dumps(req['response_params']))
    return JsonResponse({"code": 200}, safe=False)


def api_search(request):
    results = Api.objects.values().all()
    return JsonResponse({"code": 200, "records": list(results)}, safe=False)


def api_get(request):
    id = request.GET.get("id")
    result = Api.objects.filter(id=id).values().first()
    return JsonResponse({"code": 200, "record": result}, safe=False)


def api_update(request):
    req = json.loads(request.body)
    Api.objects.filter(id=req['id']).update(name=req['api_param']['name'], http=req['api_param']['http'],
                                            method=req['api_param']['method'],
                                            url=req['api_param']['url'],
                                            request_params=json.dumps(req['request_params']),
                                            response_params=json.dumps(req['response_params']))
    return JsonResponse({"code": 200}, safe=False)


def api_delete(request):
    id = request.POST.get("id")
    result = Api.objects.filter(id=id).delete()
    return JsonResponse({"code": 200, "record": result}, safe=False)