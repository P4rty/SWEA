# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 방향 0위1오2아3왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    N = int(input().strip())
    board = [list(input().strip()) for _ in range(N)]
    Q = int(input().strip())
    print(f'#{test_case}',end=' ')
    r, c, d = 0, 0, 0
    xr, xc = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                xr = i
                xc = j
                break

    for _ in range(Q):
        r, c, d = xr, xc, 0
        M, command = input().split()
        command = list(command)
        for i in range(len(command)):
            if command[i] == 'L':
                d -= 1
                if d < 0:
                    d += 4
            elif command[i] == 'R':
                d += 1
                d = (d % 4)
            elif command[i] == 'A':
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] != 'T':
                        r = nr
                        c = nc
        if board[r][c] == 'Y':
            print(1, end=" ")
        else:
            print(0, end=" ")

    print()
