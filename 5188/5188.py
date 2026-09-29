# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 각 칸에서는 오른쪽이나 아래로만 이동
dr = [1, 0]
dc = [0, 1]


def dfs(r, c, current_sum):
    global min_sum

    if current_sum >= min_sum:
        return

    if r == N - 1 and c == N - 1:
        min_sum = min(min_sum, current_sum)
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < N and nc < N:
            dfs(nr, nc, current_sum + grid[nr][nc])


for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float("inf")
    dfs(0, 0, grid[0][0])

    print(f'#{test_case} {min_sum}')
