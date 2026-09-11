# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    command = input().split()
    stack = []
    result = 'error'
    for char in command:
        if char == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
            break
        elif char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                result = 'error'
                break

            fir = stack.pop()
            sec = stack.pop()
            if char == '+':
                stack.append(sec+fir)
            elif char == '-':
                stack.append(sec-fir)
            elif char == '*':
                stack.append(sec*fir)
            elif char == '/':
                stack.append(sec//fir)

    print(f'#{test_case} {result}')
