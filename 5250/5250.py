# import sys
# sys.stdin = open("sample_input.txt", "r")
import heapq

T = int(input())

INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 최단 거리 테이블을 무한대로 초기화
    distance = [[INF] * N for _ in range(N)]
    # (비용, x, y)
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0
    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == N - 1 and y == N - 1:
            break
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 기본 이동 비용 1 + 높이 차이가 날 경우 추가 비용
                height_diff = board[nx][ny] - board[x][y]
                next_cost = cost + 1 + (height_diff if height_diff > 0 else 0)

                # 더 적은 비용으로 이동할 수 있는 경우
                if next_cost < distance[nx][ny]:
                    distance[nx][ny] = next_cost
                    heapq.heappush(queue, (next_cost, nx, ny))

    print(f'#{test_case} {distance[N - 1][N - 1]}')