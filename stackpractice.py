T = int(input())

for test_case in range(1,T+1):
    stack = []
    print('#{}'.format(test_case))

    N = int(input())
    for _ in range(N):
        command = input().split()
        if command[0] == 'i':
            stack.append(command[1])
        elif command[0]=='o':
            if len(stack)==0:
                print('empty')
            else:
                print(stack.pop())
        elif command[0]=='c':
            print(len(stack))