# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    str_1 = input()
    str_2 = input()
    dct_2 = {}
    for i in range(len(str_2)):
        if str_2[i] not in dct_2:
            dct_2[str_2[i]] = 1
        else:
            dct_2[str_2[i]] += 1
    result = 0
    for i in range(len(str_1)):
        if dct_2[str_1[i]] > result:
            result = dct_2[str_1[i]]
    print(f'#{test_case} {result}')


