# import sys
# sys.stdin = open("sample_input.txt", "r")


def hoare_partition(left, right):
    pivot = A[left]
    i = left + 1
    j = right

    while i <= j:
        # 왼쪽에서는 pivot보다 큰 값을 찾을 때까지 이동
        while i <= j and A[i] <= pivot:
            i += 1
        # 오른쪽에서는 pivot보다 작거나 같은 값을 찾을 때까지 이동
        while i <= j and A[j] >= pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    # pivot(A[left])을 자신의 최종 위치(j)로 이동
    A[left], A[j] = A[j], A[left]
    return j

def quick_sort(left, right):
    if left < right:
        # 피벗을 기준으로 좌우 분할
        pivot_index = hoare_partition(left, right)
        # 피벗 왼쪽 부분 배열 정렬
        quick_sort(left, pivot_index - 1)
        # 피벗 오른쪽 부분 배열 정렬
        quick_sort(pivot_index + 1, right)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    A = list(map(int, input().split()))

    # 퀵 정렬 구현
    # pivot 을 중심으로 기준보다 작은것을 왼편 큰것을 오른편에 위치시킴.
    # 1. 작업영역을 정한다.
    # 2. 작업 영역 중 가장 왼쪽에 있는 수를 pivot 이라고하자
    # 3. pivot 을 기준으로 왼쪽에는 pivot 보다 작은수를 배치한다.
    #   오른쪽에는 pivot 보다 큰수를 배치한다.

    quick_sort(0, N - 1)
    result = A[N//2]
    print(f'#{test_case} {result}')