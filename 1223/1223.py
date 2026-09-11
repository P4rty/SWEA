# import sys
# sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    command = list(map(str, input()))
    stack = []
    # 먼저 후위 계산식으로 바꾼다.
    lst_postfix = []
    for char in command:
        if char.isdigit():
            # command 리스트의 있는 숫자들을 후위 계산식 리스트에 추가한다.
            lst_postfix.append(char)
        elif char == '*':
            while stack and stack[-1] == '*':
                lst_postfix.append(stack.pop())
            stack.append(char)
        elif char == '+':
            while stack:
                lst_postfix.append(stack.pop())
            stack.append(char)
    # 스택에 쌓인 기호를 모두 후위 계산식 리스트에 넣는다.
    while stack:
        lst_postfix.append(stack.pop())
    # 스택 재할당
    stack = []
    for char in lst_postfix:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            fir = stack.pop()
            sec = stack.pop()
            result = int(fir) + int(sec)
            stack.append(result)
        elif char == '*':
            fir = stack.pop()
            sec = stack.pop()
            result = int(fir) * int(sec)
            stack.append(result)
    result = stack[-1]
    print(f'#{test_case} {result}')
