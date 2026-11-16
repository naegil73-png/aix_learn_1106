from django.contrib import admin
from .models import Est_wei  # 점(.)을 붙여서 현재 앱의 models.py에서 가져오도록 수정

admin.site.register(Est_wei)
