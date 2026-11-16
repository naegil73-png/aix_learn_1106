import os
import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from .models import Est_wei

# model.joblib를 불러오기 위한 경로설정 및 파일 지정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR,'model.joblib'))

def index(request):
    if request.method == 'POST':
        length = float(request.POST.get('length'))
        width = float(request.POST.get('width'))
        thick = float(request.POST.get('thick'))

        indata = np.array([[length,width,thick]])
        predict = model.predict(indata) 
        result = round(float(predict[0]),2) # 배열로 결과를 내기 때문에 숫자를 빼기 위함
        # 결과 도출

        # 결과의 저장
        Est_wei.objects.create(
            length = length,
            width = width,
            thick = thick,
            weight = result
        )

        # 전달받는 화면이 새로고침되지 않아도 되도록 전달(ajax)
        return JsonResponse({'result':result})
    
    return render(request, 'index.html')