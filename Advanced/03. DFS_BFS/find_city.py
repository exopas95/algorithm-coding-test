"""
[제목]
- 특정 거리의 도시 찾기

[내용]
- 어떤 나라에는 1~N번 까지의 도시와 M개의 단방향 도로가 존재한다.
- 모든 도로의 거리는 1인데 이때 특정한 도시 X로 부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력해라.
- 또한 출발 도시 X에서 X로 가는 최단 거리는 항상 0이다.

[입력 조건]
- 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 K가 주어진다.
- 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분한다.
- 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다.

[출력 조건]
- X로 부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
- 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""
from collections import deque

N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        for node in next_node:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                q.append(node)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)
