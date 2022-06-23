"""
[제목]
- 감시 피하기

[내용]
- N * N 크기의 복도가 있고, 이 복도는 1 * 1 크기의 칸으로 나누어지며 특정한 위치에는 선생님, 학생, 혹은 장애물이 있다.
- 현재 학생 몇 명이 수업 시간에 몰래 복도에 나왔는데, 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표이다.
- 각 선생님은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다.
- 단 복도에 장애물이 있으면 선생님은 장애물 뒤편에 숨어있는 학생을 볼 수 없다.
- 선생님은 싥이 좋아 장애물로 막히기 전까지 4가지의 방향으로 학생을 모두 볼 수 있다.
- 문제에서 위칫값을 나타낼 때는 (행, 열)의 형태로 표현한다.
- 각 칸은 선생님이 존재하면 T, 학생이 존재하면 S, 장애물이 존재하면 O로 표현한다.
- 학생들은 복도의 빈칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다.
- 그리고 장애물을 3개 설치해서 선생님의 감시로부터 모든 학생이 피할 수 있는지 계산해야 한다.
- N * N 크기의 복도에서 학생과 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력하는
- 프로그램을 작성하라.

[입력 조건]
- 첫째 줄에 자연수 N이 주어진다.
- 둘째 줄에는 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 N개의 원소가 주어지며, 공백으로 구분한다.
- 해당 위치에 학생이 있다면 S, 선생이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
- 단, 한상 빈칸의 개수는 3개 이상으로 주어진다.

[출력 조건]
- 첫째 줄에 정혹히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피할 수 있는지의 여부를 출력한다.
- 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 없다면 "NO"
"""
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))

        if board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'

    if not process():
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
