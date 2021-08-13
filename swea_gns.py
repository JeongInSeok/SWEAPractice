T = int(input())
for test_case in range(1, T+1):
    N = input()
    #각 개수를 저장하는 딕셔너리
    str_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    str_list = input().split()
    ans = ''
    # s에 'ZRO' 나 ONE 같은 문자열이 들어가면 딕셔너리의 value값을 증가시킨다.
    for i in str_list:
        str_dict[i] += 1
    #각 원소가 몇개인지 나오기때문에 앞에서부터 개수만큼 생성한다.
    for key, value in str_dict.items():
        temp = ' '.join([key] * value)
        ans += temp + ' '
    
    print('#{}'.format(test_case))
    print(ans[:len(ans) - 1])