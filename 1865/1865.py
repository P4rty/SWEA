# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(i, prob):
    global max_prob
    # 가지 치기 : 이미 구한 값보다 작으면 탐색 중단.
    if prob <= max_prob:
        return
    # 다돌아서 종료
    if i == N:
        max_prob = max(max_prob, prob)
        return

    for j in range(N):
        if not adj_n[j]:
            adj_n[j] = True
            dfs(i + 1, prob * board[i][j]/100)
            adj_n[j] = False


for test_case in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    adj_n = [False] * N

    max_prob = 0

    dfs(0, 1)
    answer = max_prob * 100

    print(f'#{test_case} {answer:.6f}')
