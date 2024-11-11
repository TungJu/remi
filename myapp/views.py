from django.shortcuts import render

# Create your views here.
from myapp.models import daily_log #引入model

def diary(request): #新增
    daily_log_list = daily_log.objects.all()
    return render(request, 'index.html',locals())