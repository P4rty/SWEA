# import sys
# sys.stdin = open("sample_input.txt", "r")


def order(node):
    global count
    if node <= N:
        order(node * 2)

        tree[node] = count
        count += 1
        order(node * 2 + 1)

T = int(input())

for test_case in range(1, T + 1):
    # N, 완전 이진트리로 만든 이진 탐색트리의 루트에 저장된 값과
    # N/2번 노드(N이 홀수 인 경우 소수점 버림) => N//2하면 됨.
    N = int(input())
    tree = [0] * (N+1)
    count = 1
    order(1)
    root = tree[1]
    target = tree[N//2]
    print(f'#{test_case} {root} {target}')
