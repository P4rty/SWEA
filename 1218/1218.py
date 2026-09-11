# import sys
# sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    # 입력 받기
    N = int(input())
    parentheses = list(map(str, input()))

    # 저번에 했던 스택으로 괄호 검사하는 것을 떠올림
    stack = []

    # 먼저 홀짝 확인
    if len(parentheses) % 2 == 1:
        result = 0
    # 길이가 짝수일 때
    else:
        # for-else 문 사용하여 for 문을 완벽히 돌았으면
        # else 문으로 가므로 break 를 편안하게 쓸 수 있음
        for parenthesis in parentheses:
            # 여는 괄호 판별
            if parenthesis in "{[(<":
                stack.append(parenthesis)
            # 닫는 괄호들 판별, 그 후 해당하는 괄호 아니면 break
            elif parenthesis == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    result = 0
                    break
            elif parenthesis == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    result = 0
                    break
            elif parenthesis == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    result = 0
                    break
            elif parenthesis == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    result = 0
                    break
        else:
            result = 1
    print(f'#{test_case} {result}')
