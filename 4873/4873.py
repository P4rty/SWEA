# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    given_input = input()
    stack = []

    for char in given_input:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    result = len(stack)
    print(f'#{test_case} {result}')
