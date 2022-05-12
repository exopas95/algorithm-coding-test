"""
[제목]
- 미래 도시

[내용]
- 도시 C에서 메시지를 보내고자 한다.
- 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때
- 도시 C에서 보낸 메시지를 받게되는 도시의 개수와 시간을 계산하라.

[입력 조건]
- 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
- 둘째 줄부터 M + 1번째 줄에 걸쳐서 ㅅ통로에 대한 X, Y, Z가 주어진다.
- 이는 특정 도시 X에서 다른 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간은 Z임을 의미한다.


[출력 조건]
- 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
"""
# %%
import heapq

INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)


# %%

# %%
