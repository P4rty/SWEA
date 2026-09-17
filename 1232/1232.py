# import sys
# sys.stdin = open("input.txt", "r")

T = 10

def postorder(node):
    if tree[node] in ['+', '-', '*', '/']:
        left_val = postorder(left_child[node])
        right_val = postorder(right_child[node])

        current = tree[node]
        if current == '+':
            return left_val + right_val
        elif current == '-':
            return left_val - right_val
        elif current == '*':
            return left_val * right_val
        elif current == '/':
            return left_val / right_val
    else:
        return tree[node]


for test_case in range(1, T + 1):
    N = int(input())

    # 부모노드 i 왼쪽 자식 i*2 오른쪽 자식 i*2 + 1
    tree = [0] * (N + 1)
    left_child = [0] * (N + 1)
    right_child = [0] * (N + 1)

    for i in range(N):
        info = input().split()
        idx = int(info[0])
        val = info[1]

        if val in ['+', '-', '*', '/']:
            tree[idx] = val
            left_child[idx] = int(info[2])
            right_child[idx] = int(info[3])
        else:
            tree[idx] = float(val)

    result = int(postorder(1))
    print(f'#{test_case} {result}')
