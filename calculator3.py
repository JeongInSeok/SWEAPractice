
# [S/W 문제해결 기본] 계산기3 
op_rank = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def PosfixChange(string):
    stk = []
    result = ''
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
    
    return result
def cal (lst):
    Stack = []
    for i in range(len(lst)):
        # 숫자면 스택에 저장
        if lst[i].isdigit():
            Stack.append(lst[i])
        # 문자일 땐 연산 후에 스택에 저장
        else:
            a = int(Stack.pop())
            b = int(Stack.pop())
            if lst[i]=='+': Stack.append(a+b)
            elif lst[i]=='*': Stack.append(b*a)
    return Stack

T=10
for test_case in range(1,T+1):
    N=int(input())
    infixArr=list(input())

    print('#{}'.format(test_case), end=' ')
    print(*cal(PosfixChange(infixArr)))
