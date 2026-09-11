import sys
sys.stdin = open("input.txt", "r")

T = 10

def is_password(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return False
    return True


for test_case in range(1, T + 1):
    # 입력
    N, password_str = input().split()
    N = int(N)
    password_lst = list(map(int, password_str))
    stack = []
    # while not is_password(password_lst):
    for i in range(len(password_lst)):
        if not stack:
            stack.append(password_lst[i])
        else:
            if password_lst[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(password_lst[i])
    password_lst = stack
    result = "".join(map(str, password_lst))
    print(f'#{test_case} {result}')

