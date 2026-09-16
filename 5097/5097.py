# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    # N , M
    N, M = map(int, input().split())
    # N개의 자연수 받기.
    num_q = list(map(int, input().split()))
    # 덱으로 변경
    num_q = deque(num_q)
    # M 번 반복
    for _ in range(M):
        # 앞에 껄 빼서
        tmp = num_q.popleft()
        # 뒤로 보내기
        num_q.append(tmp)
    result = num_q.popleft()
    print(f'#{test_case} {result}')