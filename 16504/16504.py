import sys
sys.stdin = open("in.txt","r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    gap_max = 0

    for i in range(N):
        gap_cnt = 0
        for j in range(i+1, N):
            if boxes[j] >= boxes[i]:
                gap_cnt += 1

        dist = (N - i - 1) -gap_cnt

        if dist >= gap_max:
            gap_max = dist

    print(f'#{test_case} {gap_max}')


