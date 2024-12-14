import time
start_time = time.time()

# 프로그램 소스코드
array = [3,5,1,2,4] #

summary = 0

# 모든 데이터 더하면서 합계
for x in array :
    summary += x

for i in array :
    for j in array :
        temp = i * j

end_time = time.time() # 측정 종료
print("time : ", end_time - start_time)