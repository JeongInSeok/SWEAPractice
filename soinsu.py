T = int(input())
sosu=[2, 3, 5, 7, 11]
 
for test_case in range(1, T+1):
    testnum=int(input())
    ans=[0, 0, 0, 0, 0]
    anum = 0
    for i in sosu:
        while testnum%i==0:
            testnum=testnum/i
            ans[anum] += 1
         
        anum+=1
 
    print('#{} {} {} {} {} {}'.format(test_case, ans[0], ans[1], ans[2], ans[3], ans[4]))
