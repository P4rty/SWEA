# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 입력 받기
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            # 기존 선 시작 보다 크고 , 끝보다 작을 경우
            if lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]:
                result += 1
            # 기존 선 시작 보다 작고, 끝보다 클 경우
            if lst[i][1] < lst[j][1] and lst[i][0] > lst[j][0]:
                result += 1

    print(f'#{test_case} {result}')
