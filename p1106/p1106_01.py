from sklearn import svm, metrics # svm은 데이터분류와 회귀분석에 널리 쓰이는 서포트 벡터머신 알고리즘을 모은 모듈, metrics는 성능 평가 함수 모듈

# 1. 데이터 준비 - 학습데이터, 테스트데이터 분리 8:2
# 학습데이터 : 2차원배열형태
data = [ [0,0],[0,1],[1,0],[1,1] ] # 지도학습 분류의 예제코드
label = [0,1,1,0] # 위의 []안의 합이 홀수이면 1, 짝수이면 0
# 테스트 데이터 
test_data = [[0,0],[1,0]] # 학습이 
test_label = [0,1]

# 2.데이터 학습
clf = svm.SVC()        # 알고리즘 선택
clf.fit(data, label)   # 학습시키기

# 3. 데이터 예측
results = clf.predict(test_data) # 테스트데이터를 가지고 예측실행
print("예측결과:", results)   # 0,1

# 4. 정답율
# score = metrics.accuracy_score(test_label, results)
score = clf.score(test_data, test_label) #정답율을 계산할수 있음
print("정답율:", score)   # 1.0