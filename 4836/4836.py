# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    matrix = [[0]*10 for _ in range(10)]
    N = int(input())
    paints = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(10):
            for k in range(10):
                if paints[i][0] <= j <= paints[i][2] and paints[i][1] <= k <= paints[i][3]:
                    if matrix[j][k] == 0: # 아무 색 없을 때
                        matrix[j][k] = paints[i][4]
                    elif matrix[j][k] != paints[i][4]:
                        matrix[j][k] = 3
    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1


    print(f'#{test_case} {cnt}')
