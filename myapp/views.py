import json
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse 
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timezone import make_aware, get_default_timezone
from django.utils.timezone import localtime

from myapp.models import daily_log #引入model
# from myapp.forms import daily_log_form
# Create your views here.

def calendar_page(request): 
    return render(request, 'calendar.html',locals())

# 獲取FullCalendar所有日誌事件
class AllDailyLogsView(View):
    def get(self, request):
        logs = daily_log.objects.all()
        out = []
        for log in logs:
            out.append({                                                                                       
                "title": f"精神飽滿: {log.mental}",
                "start": localtime(log.time),
                "allDay": True,
            })

        return JsonResponse(out, safe=False)
    
# class AllDailyLogsView(View):

#     def get(self, request):
#         logs = daily_log.objects.all()

#         return HttpResponse(logs)



def daily_logs_by_date(request, date):
    try:
        # 解析日期
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        # 過濾符合日期的紀錄
        logs = daily_log.objects.filter(time__date=date_obj)
        
        # 準備 JSON 回應資料
        data = []
        for log in logs:
            data.append({
                'time': log.time.strftime("%Y-%m-%d %H:%M"),
                'mental': log.mental,
                'weight': log.weight,
                'video': log.video
            })

        return JsonResponse(data, safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)


# 新增或修改日誌資料
@csrf_exempt
def daily_log_manage(request, date):
    if request.method == "POST":
        # 新增資料
        data = json.loads(request.body)
        log = daily_log.objects.create(
            time=date,
            mental=data.get("mental"),
            weight=data.get("weight"),
            video=data.get("video"),
        )
        return JsonResponse({"message": "日誌已成功新增", "date": date})

    elif request.method == "PUT":
        # 修改資料
        data = json.loads(request.body)
        # 解析日期
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        # 過濾符合日期的紀錄
        log = daily_log.objects.get(time__date=date_obj)

        log.mental = data.get("mental")
        log.weight = data.get("weight")
        log.video = data.get("video")
        log.save()
        return JsonResponse({"message": "日誌已成功更新"})

    return JsonResponse({"error": "無效的請求方法"}, status=400)