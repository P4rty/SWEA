# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 입력
    iron_razor = list(input())
    stack = []
    result = 0
    for i in range(len(iron_razor)):
        if iron_razor[i] == '(':
            stack.append(iron_razor[i])
        else: # ')'를 만날 때, 레이저 또는 막대기
            stack.pop()
            if iron_razor[i-1] == '(': # 레이저 일때
                result += len(stack)
            else: # 막대기 ( ))일 때
                result += 1

    print(f'#{test_case} {result}')