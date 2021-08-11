T = int(input())
 
for test_case in range(1, T + 1): 
    n = int(input())
    data = list(map(int, input().split()))
    ans = 0
    cnt = 0
    print(len(data))
    for i in range(0, len(data)): 
        for j in range(i+1, len(data)): 
            if data[i] > data[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt
        cnt = 0
 
    print('#{} {}'.format(test_case, ans))
