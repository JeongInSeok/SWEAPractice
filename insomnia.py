T = int(input())

for test_case in range(1,T+1):
    N= input()
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0] for _ in range(10) 으로 했으면 [ 리스트안 ] 에 [0] 이 10개 들어감 
    arr = [0 for _ in range(10)]

    cnt = 1
    # 변하지 않는 수를 따로 저장 
    constN = int(N)
    
    while 0 in arr: # 아직도 arr 배열안에 0이 있다면 반복한다.
        for i in N:
            if arr[int(i)] > 0:
                continue
            else:
                arr[int(i)] = arr[int(i)]+1
        cnt +=1
        N = str(constN * cnt)

    cnt = cnt-1

    print('# {} {}'.format(test_case, constN*cnt))
    # 문제는 몇 번 양을 센 시점을 물어봐놓고 출력결과는 왜 그 k(양을 센 횟수)N(주어진 수) 인거지???