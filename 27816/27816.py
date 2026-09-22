# import sys
# sys.stdin = open("sample_in.txt", "r")

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(start_r, start_c, N, M, board):
    queue = deque([(start_r, start_c)])
    board[start_r][start_c] = 'V'
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == "L":
                board[nr][nc] = 'V'
                queue.append((nr,nc))


T = int(input())

for test_case in range(1, T + 1):
    # 지도의 크기 받기 N by M
    N, M = map(int, input().split())
    board = [list(map(str, input())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == "L":
                result += 1
                bfs(r, c, N, M, board)




    print(f'#{test_case} {result}')

