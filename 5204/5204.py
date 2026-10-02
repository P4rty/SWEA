# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 병합 정렬
def merge_sort(numbers):
    # 하나가 될때까지 잘라준다.
    if len(numbers) == 1:
        return numbers

    # 자르는 포인트(mid)를 찾는다.
    mid = len(numbers) // 2
    # mid를 중심으로 잘라서 재귀호출 한다.
    left_nums = merge_sort(numbers[:mid])
    right_nums = merge_sort(numbers[mid:])
    # 교수님의 추가조건
    # 오른쪽 끝의 데이터가 왼쪽 끝의 데이터보다 더 작다
    if left_nums[-1] > right_nums[-1]:
        global count
        count += 1

    # 이제 left와 right를 합친다.
    new_nums = []
    left_idx = right_idx = 0
    # 왼쪽의 길이와 오른쪽의 길이를 저장
    left_n = len(left_nums)
    right_n = len(right_nums)
    # 왼쪽 또는 오른쪽의 끝에 도달할 때 까지
    while left_idx < left_n and right_idx < right_n:
        # 왼쪽이 작으면 왼쪽을, 오른쪽이 작으면 오른쪽을 넣어준다.
        if left_nums[left_idx] < right_nums[right_idx]:
            new_nums.append(left_nums[left_idx])
            # 왼쪽의 다음 원소로
            left_idx += 1
        else:
            new_nums.append(right_nums[right_idx])
            # 오른쪽의 다음 원소로
            right_idx += 1

    # 남은 애들을 넣어준다.
    while left_idx < left_n:
        new_nums.append(left_nums[left_idx])
        left_idx += 1
    while right_idx < right_n:
        new_nums.append(right_nums[right_idx])
        right_idx += 1
    return new_nums


for test_case in range(1, T + 1):
    count = 0
    n = int(input())
    nums = list(map(int, input().split()))
    nums = merge_sort(nums)
    print(f'#{test_case} {nums[n // 2]} {count}')
