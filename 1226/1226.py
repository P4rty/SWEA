# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(maze, startrow, startcol):
    visited = [[-1] * 16 for _ in range(16)]
    queue = deque([(startrow, startcol)])
    visited[startrow][startcol] = 0

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼내 출력
        r, c = queue.popleft()

        if maze[r][c] == 3:
            return 1

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에  삽입
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    return 0


T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # s : start, g: goal
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                s_r = r
                s_c = c

    result = bfs(maze, s_r, s_c)
    print(f'#{test_case} {result}')
