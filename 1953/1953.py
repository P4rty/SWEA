# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [1, 0], [1, 2], [2, 3]]


def bfs(N, M, R, C, L):
    q = [(R, C)]
    visited = [[0] * M for _ in range(N)]  # 방문 배열
    visited[R][C] = 1
    cnt = 0  # 위치 할 수 있는 총 영역 수
    while q:
        i, j = q.pop(0)
        cnt += 1
        if visited[i][j] < L:  # 시간이 남아 있는 경우
            for x in pipe[board[i][j]]:
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0 and visited[ni][nj] ==0 and (x+2) % 4 in pipe[board[ni][nj]]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return cnt


for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(N, M, R, C, L)

    print(f'#{test_case} {result}')