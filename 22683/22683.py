from collections import deque
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 방향: 상(0), 우(1), 하(2), 좌(3)
# 시작 방향은 '위'를 바라보고 시작
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 필드의 크기,나무를 벨 수 잇는 횟수
    board = [list(input().strip()) for _ in range(N)]

    # 시작점(X)과 목적지(Y) 위치 찾기
    start_r, start_c = -1, -1
    end_r, end_c = -1, -1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'X':
                start_r, start_c = r, c
            elif board[r][c] == 'Y':
                end_r, end_c = r, c
    # BFS를 위한 큐: (r, c, direction, remaining_k, cost)
    # 초기 방향: 0 (위쪽)
    queue = deque([(start_r, start_c, 0, K, 0)])
    # 방문 체크: visited[r][c][dir][remaining_k]
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    visited[start_r][start_c][0][K] = True
    answer = -1
    while queue:
        r, c, d, k, cost = queue.popleft()

        # 목적지 도달 확인
        if r == end_r and c == end_c:
            answer = cost
            break

        # 1. 제자리에서 회전하기 (왼쪽 90도, 오른쪽 90도)
        # 왼쪽 회전: (d + 3) % 4, cost + 1
        nd_left = (d + 3) % 4
        if not visited[r][c][nd_left][k]:
            visited[r][c][nd_left][k] = True
            queue.append((r, c, nd_left, k, cost + 1))

        # 오른쪽 회전: (d + 1) % 4, cost + 1
        nd_right = (d + 1) % 4
        if not visited[r][c][nd_right][k]:
            visited[r][c][nd_right][k] = True
            queue.append((r, c, nd_right, k, cost + 1))

        # 2. 앞으로 전진하기
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N:
            target = board[nr][nc]

            # 땅('G')이거나 목적지('Y')인 경우 그냥 이동
            if target in ('G', 'Y'):
                if not visited[nr][nc][d][k]:
                    visited[nr][nc][d][k] = True
                    queue.append((nr, nc, d, k, cost + 1))

            # 나무('T')인 경우, 남은 베기 횟수(k)가 있다면 벨 수 있음
            elif target == 'T' and k > 0:
                if not visited[nr][nc][d][k - 1]:
                    visited[nr][nc][d][k - 1] = True
                    queue.append((nr, nc, d, k - 1, cost + 1))

    print(f'#{test_case} {answer}')