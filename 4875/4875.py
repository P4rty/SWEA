# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # N by N의 미로 주어지고, 0은 통로 1은 벽임. 2는 출발점, 3은 도착점.
    mazeMap = [list(map(int, input())) for _ in range(N)]
    # 방향 지정 오 아  왼 위 시계방향으로 진행
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    # 현재 위치 찾기, 시작점, 시작점을 스택에 저장.
    for i in range(N):
        for j in range(N):
            if mazeMap[i][j] == 2:
                stack = [(i, j)]
                break
    result = 0
    # 본인 위치가 도착점에 도착하지 않을 때 까지 루프문 돌기
    while stack:
        r, c = stack.pop()
        mazeMap[r][c] = -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if mazeMap[nr][nc] == 3:
                    result = 1
                    break
                elif mazeMap[nr][nc] == 0:
                    stack.append((nr, nc))

    print(f'#{test_case} {result}')
