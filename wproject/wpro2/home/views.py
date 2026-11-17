import os
import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from .models import Est_wei

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = os.path.join(BASE_DIR, 'model.joblib')

def index(request):
    if request.method == 'POST':
        length = float(request.POST.get('length'))
        width = float(request.POST.get('width'))
        thick = float(request.POST.get('thick'))

        indata = np.array([[length,width,thick]])
        predict = model.predict(indata)
        result = round(float(predict[0]),2)

        Est_wei.objects.create(
            length = length,
            width = width,
            thick = thick,
            weight = result
        )

        return JsonResponse({'result':result})
    return render(request, 'index.html')