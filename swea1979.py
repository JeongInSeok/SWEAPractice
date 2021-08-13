
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    # N은 맵의 크기고 K는 단어의 길이 

    # arr = [list(map(int, input().split())) for _ in range(N)]
    Map = []
    for _ in range(N):
        Map.append(list(map(int,input().split())))
    ans = 0 

    # y값 고정하고 x값 늘려가면서 .. 가로길이 K인거 찾기

    for y in range(N):
        cnt = 0 
        for x in range(N):
            if Map[y][x]==0: # 검은 부분을 만났을 때 
                if cnt == K:
                    ans += 1
                cnt = 0 
            else: # 흰부분일 때 카운트가 하나씩 증가하고 K 단어길이와 같아지면... ans를 증가
                cnt+=1 
        if cnt==K:
            ans+=1
        
    # 세로 길이 K 인거 찾기 
    for x in range(N):
        cnt = 0 
        for y in range(N):
            if Map[y][x]==0:
                if cnt == K:
                    ans+=1
                cnt = 0
            else:
                cnt+=1
        if cnt==K:
            ans+=1
    print('#{} {}'.format(test_case, ans))
            
