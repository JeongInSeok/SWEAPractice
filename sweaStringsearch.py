T = 10
for test_case in range(1,T+1):
    ignorenum=int(input())
    ans = 0 
    searchword=input()
    crazyword=input()
    ans=crazyword.count(searchword)

    print('#{} {}'.format(test_case, ans))