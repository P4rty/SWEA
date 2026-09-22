# import sys
# sys.stdin = open("input.txt", "r")

PATTERNS = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    code_row = ""
    end_col = -1

    for r in range(N):
        if '1' in grid[r]:
            # 오른쪽에서부터 첫 번째 '1'의 위치 찾기
            end_col = grid[r].rfind('1')
            code_row = grid[r]
            break

    # '1'을 기준으로 뒤에서부터 56자리 추출
    start_col = end_col - 56 + 1
    code_str = code_row[start_col:end_col + 1]

    # 7비트씩 잘라 8개의 숫자로 변환
    numbers = []
    for i in range(0, 56, 7):
        segment = code_str[i:i + 7]
        numbers.append(PATTERNS[segment])

    # (1-based index 기준: 홀수/짝수 자리 구분)
    odd_sum = numbers[0] + numbers[2] + numbers[4] + numbers[6]  # 1, 3, 5, 7번째
    even_sum = numbers[1] + numbers[3] + numbers[5] + numbers[7]  # 2, 4, 6, 8번째

    total_val = (odd_sum * 3) + even_sum

    # 암호코드 판별 후 결과 출력
    if total_val % 10 == 0:
        result = sum(numbers)
    else:
        result = 0

    print(f"#{test_case} {result}")
