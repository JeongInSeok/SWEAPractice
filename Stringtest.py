def is_same(start_idx, str1, str2):
    n = len(str1)
    if start_idx + n -1 >= len(str2): 
        return 0
    
    for i in range(n):
        if str1[i] != str2[start_idx+i]:
            return 0
    return 1
T = int(input())
for test_case in range(1, T+1):
    str1=input()
    str2=input()
    for i in range(len(str2)):
        ret = is_same(i,str1,str2)
        if ret==1:
            flag = 1
            break
    if flag == 0:
        print("#{} 0".format(test_case))
    else:
        print("#{} 1".format(test_case))


'''
T = int(input())
for test_case in range(1, T+1):
    s = input()
    string = input()
    result = 0
    if s in string:
        result = 1
    print("#{} {}".format(test_case, result))
    '''