# import sys
# sys.stdin = open("input1.txt","r")
T = int(input())     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    result = 0
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            cnt += 1

        elif lst[i] == 0:
            cnt = 0

        if cnt >= result:
            result = cnt

    print(f'#{test_case} {result}')

