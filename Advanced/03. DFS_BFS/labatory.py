"""
[제목]
- 연구소

[내용]
- 바이러스 확산을 막기 위해 연구소에 벽을 세우려고 한다.
- 연구소의 크기가 N * M인 직사각형일 떄, 직사각형은 1 * 1 크기의 정사각형으로 이루어져있다.
- 연구소는 빈칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
- 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
- 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
- 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳이다.
- 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하라.

[입력 조건]
- 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다.
- 둘째 줄부터 N개으 ㅣ줄에 지도의 모양이 주어진다. 0은 빈칸, 1은 벽, 2는 바이러스가 있는 위치이다.
- 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
- 빈칸의 개수는 3개 이상이다.

[출력 조건]
- 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
"""
n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# 바이러스가 퍼지는 경우
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


# 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


# DFS
def dfs(count):
    global result

    # 울타리가 3개가 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
