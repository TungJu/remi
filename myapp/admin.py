from django.contrib import admin

# Register your models here.
from myapp.models import daily_log #新增

class daily_condition_Admin(admin.ModelAdmin):  #新增
    list_display = ('time', 'mental', 'weight','video') # 資料表欲顯示的欄位

admin.site.register(daily_log,daily_condition_Admin) #新增