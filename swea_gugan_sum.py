'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
'''
T = int(input())
for test_case in range(1, T+1):
    test_gugan = list(map(int, input().split()))
    listnum = list(map(int, input().split()))
    max_sum = int(-21e8)
    min_sum = int(21e8)
    ans = 0 

    for s in range(0,test_gugan[0]-(test_gugan[1]-1)):
        sum = 0
        for i in range(0,test_gugan[1]):
            sum+=listnum[s+i]
        if max_sum < sum :
            max_sum = sum
        if min_sum > sum :
            min_sum = sum  
    ans = max_sum-min_sum
    print('#{} {}'.format(test_case, ans))

