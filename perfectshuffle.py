T = int(input()) 
for test_case in range(1,T+1):
    # 단어 수
    n = int(input())
    # 단어
    words = list(map(str,input().split()))
    # 나뉘는 값
    median_num = n//2
    # 저장 공간
    res = []
    # 값을 추가할 위치 값
    idx = 1
    # 나누기
    # n이 짝수인 경우
    if n % 2 == 0:
        for q in range(n):
            if q < median_num:
                res.append(words[q])
            else:
                res.insert(idx,words[q])
                idx += 2
    else:
        for q in range(n):
            if q < median_num+1:
                res.append(words[q])
            else:
                res.insert(idx, words[q])
                idx += 2
 
    print('#{}'.format(test_case), *res)
