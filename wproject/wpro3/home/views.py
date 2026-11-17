from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
import os
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR/'model.joblib')

def ajax(request):
    data = request.POST.get('data','430,29,34,12.444,5.134')

    in_data =  data
    in_data = in_data.split(',')
    result = list(map(float,in_data))

    print('입력데이터:', result)
    result = model.predict([result])
    print(f'예측무게 : {result[0]:.2f} g')

    context = {
        'restult_data' : f'{result[0]:.2f}','result':'success'
    }
    return JsonResponse(context)