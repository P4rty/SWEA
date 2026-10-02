# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(i, price):
    global min_price
    # 가지 치기 : 이미 구한 값보다 크면 탐색 중단.
    if price >= min_price:
        return
    # 다돌아서 종료
    if i == N:
        min_price = min(min_price, price)
        return

    for j in range(N):
        if not adj_n[j]:
            adj_n[j] = True
            dfs(i + 1, price + board[i][j])
            adj_n[j] = False


for test_case in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    adj_n = [False] * N

    min_price = float("inf")

    dfs(0, 0)
    answer = min_price

    print(f'#{test_case} {answer}')
