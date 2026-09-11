# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    given_input = [input().strip() for _ in range(5)]
    for i in range(5):
        given_input[i] = list(given_input[i])
    board = [[0 for _ in range(15)] for _ in range(5)]
    for i in range(5):
        for j in range(15):
            if j < len(given_input[i]):
                board[i][j] = given_input[i][j]
    print(f'#{test_case}', end=" ")
    for j in range(15):
        for i in range(5):
            if board[i][j] != 0:
                print(board[i][j], end="")
    print()
