
T = int(input())
for tc in range(1,T+1):
    h1, h2 = map(int, input().split())
    res = (h1+h2)%24
    print('#{} {}'.format(tc,res))