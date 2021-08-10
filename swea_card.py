'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
T = int(input())
for test_case in range(1, T+1):
    cardsu = int(input())
    cardnum=int(input())

    cardnum = str(cardnum)
    max_num = int(-21e8)
    num_count = 0
    ans_count=0

    for num in range(10):
        num_count=cardnum.count(str(num))
        if ans_count<num_count:
            max_num=num
            ans_count=num_count
        if ans_count==num_count:
            max_num=num
            ans_count=num_count
    print('#{} {} {}'.format(test_case, max_num, ans_count))
        
