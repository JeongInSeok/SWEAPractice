T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = [[0] * 11 for _ in range(11)]
    cnt = 0
    for n in range(N):
        a= list(map(int, input().split()))
        # ex 2 2 4 4 1 (마지막 숫자는 색깔 지정)
        for i in range(a[0],a[2]+1): # y축 ex) 2~4 까지
            for j in range(a[1],a[3]+1): # 열 , ex 2 ~ 4까지 
                if lst[i][j] ==1:
                    lst[i][j]=3
                    cnt+=1
                elif lst[i][j] ==2:
                    lst[i][j] =3
                    cnt +=1
                else:
                    lst[i][j] = a[4] # 일단 처음에 a[4] = 1 빨강색으로 칠하고 다음에 3 3 6 6 2 입력하면 2로 갈아치워짐. 
  
    print(f'#{t} {cnt}')