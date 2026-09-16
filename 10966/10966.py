# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]




T = int(input())

for test_case in range(1, T + 1):
    # 지도의 크기 받기 N by M
    N, M = map(int, input().split())
    board = [list(map(str, input())) for _ in range(N)]
    # start 가 많으므로 N*M - 물의 개수이므로
    # L의 위치를 담는 리스트 추가. 했는데 시간초과가 나므로,
    loc_lst = []
    result = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == "W":
                loc_lst.append([r, c])
    visited = [[-1] * M for _ in range(N)]
    # startlst 형식 [[r1,c1],[r2,c2],[r3,c3], ... ]
    queue = deque(loc_lst)
    for r, c in loc_lst:
        visited[r][c] = 0
    result = 0
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼내 출력
        r, c = queue.popleft()

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에  삽입
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    result += visited[nr][nc]
                    queue.append((nr,nc))

    print(f'#{test_case} {result}')
