"""
[제목]
- 미래 도시

[내용]
- 1번부터 N번까지의 회사가 있는데 특정 회사끼리 서로 도로를 통해 연결되어 있다.
- A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 팔고자 한다.
- 도로를 이용해야하며 양방향으로 이동할 수 있다. 
- 특정 회사에서 다른 회사가 도로로 연결되어 있다면 정확히 1만큼의 시간으로 이동 할 수 있다.
- 또한 A는 K번 회사에 있는 소개팅 상대에게도 가야한다.
- 물건을 팔기 전 1번 회사에서 출발하여 K번 회사에 간 후 X번 회사에 도착하는 것이 목표다.
- 이때 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하라.

[입력 조건]
- 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다. (1<=N, M<=100)
- 둘째 줄 부터 M + 1 번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
- M + 2 번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 <= K <= 100)

[출력 조건]
- 첫째 줄에 방문 판매원 A가 K번회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
- 만약 도달 할 수 없다면 01을  출력한다.
"""
# %%
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

print(graph)
# %%

# %%
