"""
[제목]
- 도시 분할 계획

[내용]
- 마을이 N개의 집과 M개의 길로 이루어져 있다. 깅른 어느 방향으로든지 다닐 수 있다.
- 마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
- 이때 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야한다.
- 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다.
- 마을에는 적어도 하나 이상의 집이 있어야 한다.
- 분리된 마을 두 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
- 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 없앨 수 있다.
- 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.

[입력 조건]
- 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.
- 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데
- A번과 B번 집을 연결하는 길의 유지비가 C라는 뜻이다.

[출력 조건]
- 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.
"""
# %%
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
