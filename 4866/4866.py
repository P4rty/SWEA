# import sys
# sys.stdin = open("sample_input.txt", "r")

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.items.pop()

T = int(input())

for test_case in range(1, T + 1):
    given_input = input()
    result = 1
    lst_check = []

    for char in given_input:
        if char == '(':
            lst_check.append(char)
        elif char == '{':
            lst_check.append(char)
        elif char == ')':
            if not lst_check or lst_check[-1] != '(':
                result = 0
                break
            lst_check.pop()
        elif char == '}':
            if not lst_check or lst_check[-1] != '{':
                result = 0
                break
            lst_check.pop()

    if len(lst_check) != 0:
        result = 0
    print(f'#{test_case} {result}')
