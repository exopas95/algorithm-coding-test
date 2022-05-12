"""
[제목]
- 뱀
- 링크: https://acmicpc.net/problem/3190

[내용]
- 뱀이 기어다니는데 사과를 먹으면 뱀의 길이가 늘어난다.
- 뱀은 처음에 오른쪽을 향한다.
- 뱀은 게임을 시작할 때 맨 위 좌측에 위치하고 뱀의 길이는 1이다.
- 뱀은 매초마다 움직이며 다음 규칙을 따른다.
- 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
- 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
- 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸 길이는 변하지 않는다.

[입력 조건]
- 첫째 줄에 보드의 크기 N이 주어진다. 다음 줄에 사과의 개수 K가 주어진다.
- 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
- 사과의 위치는 모두 다르며, 맨 위 맨 좌측에는 사과가 없다.
- 다음 줄에는 뱀의 방향 변환 횟수 L이 주어진다.
- 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며
- 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다.
- 방향 전환 정보는 X가 증가하는 순으로 주어진다.

[출력 조건]
- 첫쨰 줄에 게임이 몇 초에 끝나는지 출력한다.
"""

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(1):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction


def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0

    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())
