T = int(input())
for test_case in range(1,T+1):
    user_input = input()
    stack = []
    for s in user_input:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
    print('#{} {}'.format(test_case, len(stack)))