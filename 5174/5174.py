# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def count_subtree_nodes(node):
    if node == 0:  # 자식이 없는 경우
        return 0

    # 현재 노드(1) + 왼쪽 서브트리 노드 수 + 오른쪽 서브트리 노드 수
    return 1 + count_subtree_nodes(ch1[node]) + count_subtree_nodes(ch2[node])


for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    parent_child = list(map(int, input().split()))

    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(0, len(parent_child), 2):
        parent, child = parent_child[i], parent_child[i + 1]
        if ch1[parent] == 0:
            ch1[parent] = child
        else:
            ch2[parent] = child

    result = count_subtree_nodes(N)
    print(f"#{test_case} {result}")