"""
[제목]
- 경쟁적 전염

[내용]
- N * N 크기의 시험관이 있고 시험관은 1 * 1 크기의 칸으로 나뉘어져 있다.
- 특정한 위치에는 바이러스가 존재할 수 있다.
- 바이러스의 종류는 1 ~ K번 까지 K 가지가 있으며 모든 바이러스는 이 중 하나에 속한다.
- 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식한다.
- 매초 번호가 낮은 종류의 바이러스부터 먼저 증식하며 증식 과정에서 특정한 칸에 이미어떠한 바이러스가 있다면, 다른 바이러스가 들어갈 수 없다.
- 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때 S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하라.
- 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면 0을 출력한다.
- 이때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1, 1)에 해당한다.
- 모든 도로의 거리는 1인데 이때 특정한 도시 X로 부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력해라.
- 또한 출발 도시 X에서 X로 가는 최단 거리는 항상 0이다.

[입력 조건]
- 첫쨰 줄에 자연수 N, K가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며
- 해당 위치에 존재하는 바이러스의 번호가 주어지며 공백으로 구분한다.
- 단 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다.
- 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다.
- N + 2번째 줄에는 S, X, Y가 주어지며 공백으로 구분한다.

[출력 조건]
- S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력하고 만약 없으면 0을 출려한다.
"""
from collections import deque

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
