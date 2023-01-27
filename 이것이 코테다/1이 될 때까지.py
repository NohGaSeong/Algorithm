'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.
'''
count = 0
n, m = map(int, input().split())

while True:
    if n % m == 0 :
        n = int(n / m)
        count += 1
    elif n == 1:
        break
    else :
        n -= 1
        count += 1

    

print(count)
