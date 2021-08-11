T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    # 1<<n : 부분 집합의 갯수 
    for i in range(1 << N):  # 만약 공집합 제외한 다면? range(1, 1<<n)
        sum = 0
        for j in range(N):  # 원소(배열의 요소) 의 수 만큼 비트를 비교한다.
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소를 출력 
                sum += arr[j]
 
        if sum == 0:
            ans += 1
 
    print('#{} {}'.format(test_case, ans))