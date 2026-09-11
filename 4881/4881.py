# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def dfs(row, current_sum):
    global min_sum
    # 현재 누적합이 기존 최소합보다 클경우 필요없어짐
    if current_sum >= min_sum:
        return  # break 한다고 생각하면 됨
    if row == N:  # 이미 모든 값을 놓은 경우
        min_sum = current_sum
        return  # break  한다고 생각하면 됨
    for col in range(N):  # 모든 열에 대해 DFS & Backtracking
        if not visited[col]:  # 방문 했는지 안했는 지 확인.
            visited[col] = True
            dfs(row+1, current_sum + board[row][col])
            visited[col] = False  # 다 돌고 다른 선택지에서 선택지가 되도록 다시 false 처리


for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]  # N by N 행렬 입력받음.

    visited = [False] * N
    min_sum = sum(sum(row) for row in board)
    dfs(0, 0)

    print(f'#{test_case} {min_sum}')
