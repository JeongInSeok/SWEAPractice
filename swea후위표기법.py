# 후위표기법 
'''
1+2*3 => 123*+
'''
op_rank = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
 
T = int(input())
 
for t in range(1, T+1):
    string = input().rstrip()
 
    result = ''
    stk = []
    for c in string:
        if c.isdigit():
            result += c
            continue
        # 스택에 쌓여있는게 없고 열린 괄호를 만났을 때 ( 스택에 push한다.   
        if len(stk) == 0 or c == '(':
            stk.append(c)
            continue
        # 닫힌 괄호 ')'를 만나면 열린괄호가 나올 때 까지 스택에서 pop해서 출력한다.
        if c == ')':
            while stk[-1] != '(':
                result += stk.pop()
            stk.pop()
            continue
        # 연산자는 스택에서 이보다 높은 우선순위 것들을 pop 해서 출력한다. 
        while len(stk) and op_rank[stk[-1]] >= op_rank[c]:
            result += stk.pop()
 
        stk.append(c)
 
    while len(stk):
        result += stk.pop()
 
    print('#{} {}'.format(t, result))
