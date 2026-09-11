import sys
sys.stdin = open("input.txt","r")
for test_case in range(1, 11):
    N = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))
    result = 0
    for _ in range(N):
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
    result = max(boxes) - min(boxes)
    print(f'#{test_case} {result}')
