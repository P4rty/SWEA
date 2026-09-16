# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(maze, startrow, startcol, N):
    visited = [[-1] * N for _ in range(N)]
    queue = deque([(startrow, startcol)])
    visited[startrow][startcol] = 0

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼내 출력
        r, c = queue.popleft()

        if maze[r][c] == 3:
            return visited[r][c] -1

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에  삽입
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    return 0



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # s : start, g: goal
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                s_r = r
                s_c = c

    result = bfs(maze, s_r, s_c, N)

    print(f'#{test_case} {result}')