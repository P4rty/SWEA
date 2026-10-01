# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # A 와 B 에 속한 정수의 개수 N, M
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))

    # 이진 탐색의 왼쪽구간은 l 부터 m - 1,
    # 오른쪽 구간은 m + 1 부터 r 이 된다.
    # m = (l + r) // 2
    # 찾아야하는 값. 오른쪽 하고 왼쪽 찾는 값 또는 왼쪽하고 오른쪽 찾는 값...
    result = 0
    # 왼쪽, 오른쪽 구분해서, 그냥 같은 방향 되버리면 바로 break 시켜버리기
    # 왼쪽은 1, 오른쪽 2

    for target in M_list:
        # 이진탐색
        l = 0
        r = len(N_list) - 1
        direction = 0
        while l <= r:
            m = (l + r) // 2
            if target == N_list[m]:
                result += 1
                break

            elif target > N_list[m]:
                # 오른쪽임
                if direction == 2:
                    # 탐색 할 필요 없음 바로 가지치기
                    break
                else:
                    # 탐색해야함.
                    l = m + 1
                    direction = 2
            elif target < N_list[m]:
                # 왼쪽일 경우
                if direction == 1:
                    # 탐색할 필요 없이 가지치기
                    break
                else:
                    r = m - 1
                    direction = 1



    print(f'#{test_case} {result}')
