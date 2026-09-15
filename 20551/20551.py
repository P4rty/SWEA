# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    lst = list(map(int, input().split()))
    while lst[0] > lst[1] - 1:
        lst[0] -= 1
        result += 1
        if lst[0] == 0:
            result = -1
            break
    if result == -1:
        pass
    else:
        while lst[1] > lst[2] - 1:
            lst[1] -= 1
            result += 1
            if lst[1] == 0:
                result = -1
                break
            if lst[1] == lst[0]:
                result += 1
                lst[0] -= 1

    print(f'#{test_case} {result}')
