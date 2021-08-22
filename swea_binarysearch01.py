def binarysearch(arr, val):
    start, end = 1, arr
    count = 0
    while start <= end:
        index = (start+end)//2
        count += 1

        if index == val:
            return count
        elif index < val:
            start = index
        elif index > val:
            end = index
    return -1 


T = int(input())
for test_case in range(1, T+1):
    P, ap, bp = map(int,input().split())
    # P는 책의 page 수 1 ~ 400
    # ap는 A가 찾을 page 번호 bp는 B가 찾을 쪽 번호
    ac = binarysearch(P, ap)
    bc = binarysearch(P, bp)
    ans = ''
    if ac < bc:
        ans = 'A'
    elif ac > bc:
        ans = 'B'
    else:
        ans ='0'

    print('#{} {}'.format(test_case,ans))