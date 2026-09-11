# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    str_1 = input()
    str_2 = input()
    correct = 0
    for i in range(len(str_2)-len(str_1)+1):
        if str_1 == str_2[i:i+len(str_1)]:
            correct = 1
    print(f'#{test_case} {correct}')
