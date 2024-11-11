from django.db import models

# Create your models here.
class daily_log(models.Model):
    time = models.DateTimeField(primary_key=True)
    mental = models.CharField(max_length=2)# 精神
    weight = models.CharField(max_length=5, blank=True) # 體重
    # temperature = models.CharField(max_length=3, blank=True) # 體溫
    # food = models.CharField(max_length=2)# 飲食
    # water  = models.CharField(max_length=2)# 飲水
    # excretion = models.CharField(max_length=2)# 廁所
    # Trim_nails = models.CharField(max_length=2)# 剪指甲
    # 嘔吐
    # 接種疫苗
    # 藥
    # 紀念日
    video = models.CharField(max_length=25, blank=True)# 影片