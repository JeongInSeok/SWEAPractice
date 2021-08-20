
T=int(input())
for test_case in range(1,T+1):
    a,b = input().split()
    print('#{} {}'.format(test_case, len(a)-(len(b)-1)*a.count(b)))