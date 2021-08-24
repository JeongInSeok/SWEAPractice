
# 구간별 최대, 최소 구하기 ( 50점 )
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    # N개의 정수가 들어 있는 배열
    # 이웃한 M개의 숫자 중 가장 큰 값과 작은 값
    lis = list(map(int,input().split()))
    chai = []
    # chai는 차이 영어가 안 떠올라서 maxnum 과 minnum의 차이를 표현한 것입니다.
    for i in range(N-M+1): # 연산 실시 횟수
        maxnum = 0
        minnum = 10001
        for j in range(M):
            if maxnum<lis[i+j]:
                maxnum=lis[i+j]
            if minnum>lis[i+j]:
                minnum=lis[i+j]
        chai.append(maxnum-minnum)

    print('#{}'.format(test_case), end=' ')
    print(*chai)