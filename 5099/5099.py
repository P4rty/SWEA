# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    # N 개의 피자 동시에 구움, M개가 주어짐.
    N, M = map(int, input().split())
    # M개의 pizza 받기.
    pizza_waiting = list(map(int, input().split()))
    pizza_fire = deque()
    for i in range(N):
        pizza_fire.append([pizza_waiting[i], i+1])

    idx = N
    result = 0
    while pizza_fire:
        cheese = pizza_fire.popleft()
        cheese[0] //= 2
        if cheese[0] > 0:
            pizza_fire.append(cheese)
        else:
            # 피자의 치즈가 녹았으면, 빼내고 다음꺼 넣어야함.
            result = cheese[1]
            if idx < M:
                pizza_fire.append([pizza_waiting[idx], idx + 1])
                idx += 1

    print(f'#{test_case} {result}')