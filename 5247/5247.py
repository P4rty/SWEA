# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

T = int(input())

# 연산 리스트
# +1, -1, *2, -10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    MAX = 10 ** 6
    # 최소횟수 구하는 거니까 bfs임.
    used = [0] * (MAX + 1)
    q = deque()
    q.append((N, 0))
    used[N] = 1
    result = -1
    while q:
        now, check = q.popleft()
        if now == M:
            result = check
            break
        for nxt in (now + 1, now - 1, now * 2, now - 10):
            if 1 <= nxt <= MAX and not used[nxt]:
                used[nxt] = 1
                q.append((nxt, check + 1))

    print(f'#{test_case} {result}')