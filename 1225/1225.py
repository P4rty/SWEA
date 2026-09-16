# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

T = 10
for test_case in range(1, T + 1):
    # 테스트 케이스의 번호
    trash = int(input())
    # 8개의 데이터 받기.
    num = list(map(int, input().split()))
    # 덱으로 변경
    num = deque(num)
    # 0보다 작아지는 경우 0이됨.
    cnt = 1
    # 종료조건 없어도 상관이 없기에 무한 반복으로 해놓음.
    while True:
        # 앞에 껄 빼서
        tmp = num.popleft()
        tmp -= cnt
        cnt += 1
        # 한사이클이 지났으므로 초기화
        if cnt == 6:
            cnt = 1
        # 만약 음수가 나오면 0으로 넣고 마무리.
        if tmp <= 0:
            num.append(0)
            break
        # 뒤로 보내기
        num.append(tmp)

    result = num
    print(f'#{test_case}', end=" ")
    print(*result)