# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 카운트하는 결과값
    result = 0
    # 입력 받기
    lst = list(map(int, input().split()))
    # lst[0]이 lst[1] - 1 보다 커질 때 까지
    while lst[0] > lst[1] - 1:
        lst[0] -= 1
        result += 1
        # 행동
        if lst[0] == 0:
            result = -1
            break
    # 앞에서 한 것이 에러가 나면 다음 반복문 넘어가기
    if result == -1:
        pass
    else:
        # 같은 반복
        while lst[1] > lst[2] - 1:
            lst[1] -= 1
            result += 1
            if lst[1] == 0:
                result = -1
                break
            # 같아질 경우 맨앞을 빼고 결과 값 증가시킴.
            if lst[1] == lst[0]:
                result += 1
                lst[0] -= 1

    print(f'#{test_case} {result}')
