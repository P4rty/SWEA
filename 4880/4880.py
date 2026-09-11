# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def rcp(i, j, lst): # 가위 바위 보 (1,2,3),
    a, b = lst[i-1], lst[j-1]

    if a == b:
        return i
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        return i
    return j


def dual(i, j, lst):
    if i == j:
        return i

    mid = (i+j) // 2
    left_winner = dual(i, mid, lst)
    right_winner = dual(mid + 1, j, lst)

    return rcp(left_winner, right_winner, lst)


for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    card_N = list(map(int, input().split()))

    result = dual(1,N, card_N)

    print(f'#{test_case} {result}')
