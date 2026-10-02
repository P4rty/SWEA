# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(pos, cnt):
    global min_cnt
    # 가지 치기 : 이미 구한 값보다 크면 탐색 중단.
    if cnt >= min_cnt:
        return
    # 넘어가서 종료
    if pos >= N - 1:
        min_cnt = min(min_cnt, cnt)
        return
    battery = board[pos]
    for i in range(battery, 0, -1):
        dfs(pos + i, cnt + 1)


for test_case in range(1, T + 1):
    board = list(map(int, input().split()))
    N = board[0]
    board = board[1:]

    min_cnt = float("inf")
    dfs(0, 0)
    answer = min_cnt - 1

    print(f'#{test_case} {answer}')
