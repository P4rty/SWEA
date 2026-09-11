# import sys
# sys.stdin = open("input.txt","r")
T = 10     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    max_row_sum = float('-inf')
    max_column_sum = float('-inf')
    # 행,열, 대각선 순
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    for i in range(len(lst)):
        tmp_column_sum = 0
        tmp_row_sum = 0
        left_diagonal_sum += lst[i][i]
        right_diagonal_sum += lst[i][99-i]
        for j in range(len(lst)):
            tmp_row_sum += lst[i][j]
            tmp_column_sum += lst[j][i]
        if max_row_sum <= tmp_row_sum:
            max_row_sum = tmp_row_sum
        if max_column_sum <= tmp_column_sum:
            max_column_sum = tmp_column_sum
    result = max(max_row_sum, max_column_sum, left_diagonal_sum, right_diagonal_sum)
    print(f'#{test_case} {result}')

