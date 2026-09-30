# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 트럭에서 제일 큰거 부터 시작해서 가져가기
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    # truck_idx : 트럭쪽 인덱스
    # cnt : 컨테이너 인덱스
    # result : 결과값
    truck_idx = 0
    cnt = 0
    result = 0
    while truck_idx < len(trucks):

        # 트럭이 컨테이너보다 큰경우
        if trucks[truck_idx] >= containers[cnt]:
            truck_idx += 1
            result += containers[cnt]
            cnt += 1

        # 트럭이 컨테이너보다 작은 경우
        else:
            cnt += 1
        if cnt >= len(containers):
            break

    print(f'#{test_case} {result}')
