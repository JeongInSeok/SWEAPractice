
def DFS(now):
    for next in range(1, V+1):
        if Map[now][next] == 0 : continue
        if visited[next]==1: continue
        visited[next]=1
        DFS(next)
    return

T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())

    # 그래프로 각 노드별 어느 노드로 갈 수 있는 길을 표시하는 Map 
    Map = [[0]*(V+1) for _ in range(V+1)] 
    visited = [0]*(V+1) # 방문을 표시하는 리스트

    for i in range(E): # 간선의 수 만큼 반복함.
        start, end = map(int,input().split()) # 간선을 입력 받는다.
        Map[start][end] = 1
        
    # 경로의 존재를 확인하는 출발노드 S 도착노드 G
    start_node, end_node = map(int, input().split())
    visited[start_node]=1

    DFS(start_node)
    if visited[end_node]==1:
        print('#{} {}'.format(test_case, 1))
    else: 
        print('#{} {}'.format(test_case, 0))