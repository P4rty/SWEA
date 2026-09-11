# import sys
# sys.stdin = open("input.txt", "r")
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    result = 0
    # 행 비교
    for r in range(8):
        for c in range(8-N+1):
            compare_str = board[r][c:c+N]
            if compare_str == compare_str[::-1]:
                result += 1
    # 열 비교
    for c in range(8):
        for r in range(8 - N + 1):
            compare_str = "".join(board[r+k][c] for k in range(N))
            if compare_str == compare_str[::-1]:
                result += 1

    print(f'#{test_case} {result}')