
def paper(n):
    if n==1:
        return 1
    elif n==2:
        return 3
    return paper(n-1) + (2*paper(n-2))
 
T= int(input())
for t in range(1,T+1):
    n= int(input())
    cnt = paper(n//10)
    print("#{} {}".format(t,cnt))