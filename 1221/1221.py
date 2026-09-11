# import sys
# sys.stdin = open("GNS_test_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    trash, N = input().split()
    board = list(map(str,input().split()))
    lng_alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(board)):
        for j in range(len(lng_alien)):
            if board[i] == lng_alien[j]:
                board[i] = j
    board = sorted(board)
    for i in range(len(board)):
        for j in range(len(lng_alien)):
            if board[i] == j:
                board[i] = lng_alien[j]
    result = " ".join(board)

    print(f'#{test_case} {result}')