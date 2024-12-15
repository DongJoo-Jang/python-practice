#내가 작성한코드
"""
n, m = map(int, input().split())
result = n
count = 0
while result != 1 :
    if result % m  == 0 :
        result = result / m
    else :
        result -= 1
    count += 1

print(count)
"""

#책에 나온 코드
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k :
    # N이 K로 나누어 떨어지지 않느다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K 로 나누기
    n //= k
    result += 1
    





