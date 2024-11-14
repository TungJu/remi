import json
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import JsonResponse 
from django.utils import timezone

from myapp.models import daily_log #引入model
# from myapp.forms import daily_log_form
# Create your views here.
def diary(request): 
    daily_log_list = daily_log.objects.all()
    return render(request, 'index.html',locals())

class MyReportView(View):

    def get(self, request):
        ret = dict()
        my_report_all = daily_log.objects.all()
        ret['my_report_all'] = my_report_all
        return render(request, 'index.html',locals())


def all_daily_log(request):                                                                                                 
    all_daily_log = daily_log.objects.all()
    out = []
    for i in all_daily_log:
        out.append({                                                                                       
            'time' : i.time.strftime("%Y/%m/%d"),                                                         
            'mental' : i.mental,
            'weight' : i.weight,
            'video' : i.video,
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add(request):

    if request.method == "POST":
        time_str = request.POST.get("time", None)
        naive_time = timezone.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        aware_time = timezone.make_aware(naive_time, timezone.get_current_timezone())
        mental = request.POST.get("mental", None)
        weight = request.POST.get("weight", None)
        video = request.POST.get("video", None)
        log = daily_log(time=aware_time, mental=mental, weight=weight,video=video)
        log.save()
        data = {}
        return JsonResponse({"message": "Added Successfully"})
    else:
        # 如果請求方法不是 POST，返回錯誤回應
        return JsonResponse({"error": "Invalid request method"}, status=400)
 
# def update(request):
#     start = request.GET.get("start", None)
#     end = request.GET.get("end", None)
#     title = request.GET.get("title", None)
#     id = request.GET.get("id", None)
#     event = Events.objects.get(id=id)
#     event.start = start
#     event.end = end
#     event.name = title
#     event.save()
#     data = {}
#     return JsonResponse(data)