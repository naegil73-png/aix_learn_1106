from django.contrib import admin
from .models import Est_wei

@admin.register(Est_wei) # Est_wei 등록 명령
class EstweiAdmin(admin.ModelAdmin): # Est_wei를 어떻게 보여 줄지 설계도 만들어라
    list_display = ('id', 'length', 'width', 'thick', 'weight', 'created_at') # 고유번호, 길이, 너비, 두께, 무게, 저장날자