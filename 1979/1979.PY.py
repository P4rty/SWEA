import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    lst_c = []
    lst_r = []
    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if lst[i][j] == 1:
                cnt_r += 1
            elif lst[i][j] == 0:
                lst_r.append(cnt_r)
                cnt_r = 0
        if lst[i][N-1] == 1:
            lst_r.append(cnt_r)

    for i in range(N):
        cnt_c = 0
        for j in range(N):
            if lst[j][i] == 1:
                cnt_c += 1
            elif lst[j][i] == 0:
                lst_c.append(cnt_c)
                cnt_c = 0
        if lst[N-1][i] == 1:
            lst_c.append(cnt_c)

    for i in range(len(lst_r)):
        if lst_r[i] == K:
            result += 1
    for i in range(len(lst_c)):
        if lst_c[i] == K:
            result += 1

    print(f'#{test_case} {result}')
