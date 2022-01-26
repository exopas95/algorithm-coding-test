'''
[제목]
- 게임 개발

[문제]
- 1단계: 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
- 2단계: 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진한다.
-       왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽방향으로 횐전만 수행하고 1단계로 돌아간다.
- 3단계: 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로
-       한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

[입력 조건]
- 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을공백으로 구분하여 입력한다. (3 <= N, M <= 50)
- 둘째 줄에 게임 캐릭터가 있는 칸의 좌표( A,B)와 바라보는 방향 d가 서로 공백으로 구분하여 주어진다.
- 방향 d의값으로는 다음과 같이 4가지가 존재한다
- 0: 북쪽
- 1: 동쪽
- 2: 남쪽
- 3: 서쪽
- 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로,
- 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바도로 되어 있다.
- 0: 육지
- 1: 바다

[출력 조건]
- 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸 수를 출력한다.
'''

# %%
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

real_map = []
for i in range(n):
    real_map.append(list(map(int, input().split())))

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def turn_left():
    global direction
    direction -= 1

    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and real_map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if real_map[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)
# %%
