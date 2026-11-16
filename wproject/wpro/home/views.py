import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from django.shortcuts import render
from django.http import JsonResponse
from .models import Est_wei

# [임시 모델 설정] .pkl 파일 에러를 방지하기 위해 뷰 내부에서 간단히 모델과 전처리기를 생성합니다.
# (실제 학습된 모델 객체가 있다면 해당 객체로 대체하시면 됩니다.)
poly = PolynomialFeatures(include_bias=False)
ss = StandardScaler()
ridge = Ridge()

# 임의의 데이터로 뼈대 학습 (서버 실행 시 에러 방지용)
X_train_dummy = np.array([[10, 5, 2], [20, 10, 4], [30, 15, 6]])
y_train_dummy = np.array([100, 300, 600])
X_poly_dummy = poly.fit_transform(X_train_dummy)
X_scale_dummy = ss.fit_transform(X_poly_dummy)
ridge.fit(X_scale_dummy, y_train_dummy)


def index(request):
    if request.method == "POST":
        # 1. 입력값 가져오기
        length = float(request.POST.get('length', 0))
        width = float(request.POST.get('width', 0))
        thick = float(request.POST.get('thick', 0))

        # 2. 2차원 배열 변환 및 머신러닝 예측
        indata = np.array([[length, width, thick]])
        indata_poly = poly.transform(indata)
        indata_inscale = ss.transform(indata_poly)
        predict = ridge.predict(indata_inscale)
        predict_result = round(predict[0], 2)

        # 3. 데이터베이스 저장
        Est_wei.objects.create(
            length=length,
            width=width,
            thick=thick,
            weight=predict_result
        )

        # 4. 팝업창(fetch)으로 결과 반환
        return JsonResponse({'predict_result': predict_result})

    return render(request, 'index.html')