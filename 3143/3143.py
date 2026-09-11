# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    cnt = 0
    target, shortcut = input().split(" ")
    shortcut_len = len(shortcut)
    while result < len(target):
        if target[result:result + shortcut_len] == shortcut:

            result += shortcut_len
            cnt += 1
        else:
            result += 1
            cnt += 1

    print(f'#{test_case} {cnt}')