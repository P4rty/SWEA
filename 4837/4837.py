T = int(input())
A = list(range(1, 13))
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0      # 만족시키는 부분집합의 개수
    for i in range(1 << 12):    # 모든 부분 집합 탐색 2^12개수
        cnt = 0
        sum_num = 0
        for j in range(12):
            if i & (1 << j):
                sum_num += A[j]
                cnt += 1
        if cnt == N and sum_num == K:
            result += 1     # 만족시키는 경우 +1
    print(f'#{test_case} {result}')