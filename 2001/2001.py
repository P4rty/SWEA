import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += lst[i + k][j + l]
            if cnt > result:
                result = cnt

    print(f'#{test_case} {result}')
