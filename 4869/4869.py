# import sys
# sys.stdin = open("sample_input.txt", "r")


def func(n):
    if n < 2:
        return 1
    return func(n-1) + func(n-2) * 2


T = int(input())

for test_case in range(1, T + 1):
    given_input = int(input())
    result = func(given_input//10)
    print(f'#{test_case} {result}')
