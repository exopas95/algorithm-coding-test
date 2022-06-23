"""
[제목]
- 블록 이동하기

[내용]
- 로봇은 2 * 1 크기의 로봇으로 0과 1로 이루어진 N * N 크기의 지도에서 2* 1 크기의 로봇을 움직여 (N, N) 위치까지 이동할 수 있도록 하려고 한다.
- 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 0은 빈칸을, 1은 벽을 나타낸다.
- 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없다.
- 로봇은 좌표 (1,1) 위치에서 가로 방향으로 놓여 있는 상태로 시작하며, 앞뒤 구분 없이 움직일 수 있다.
- 로봇이 움지일 때는 현재 놓여 있는 상태를 유지하면서 이동한다.
- 로봇은 90도씩 회전할 수있다.
- 단 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향에 벽이 업어야 한다.
- 로봇이한칸 이동하거나 90도 회전하는데 걸리는 시간은 정확히 1초이다.
- 0ㅘ 1로 이루어진 지도 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 리턴하세요

[제한 사항]
- board의 한 변의 길이는 5이상 100 이하이다.
- board의 원소는 0 또는 1 이다.
- 로봇이 처음 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어진다.
- 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어진다.
"""

# 파이썬
from collections import deque


def can_move(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    # 평행이동
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in DELTAS:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1, nxt2))
    # 회전
    if cur1[Y] == cur2[Y]:  # 가로방향 일 때
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y] + d][cur2[X]] == 0:
                cand.append((cur1, (cur1[Y] + d, cur1[X])))
                cand.append((cur2, (cur2[Y] + d, cur2[X])))
    else:  # 세로 방향 일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X] + d] == 0 and new_board[cur2[Y]][cur2[X] + d] == 0:
                cand.append(((cur1[Y], cur1[X] + d), cur1))
                cand.append(((cur2[Y], cur2[X] + d), cur2))

    return cand


def solution(board):
    # board 외벽 둘러싸기
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
                que.append((*nxt, count + 1))
                confirm.add(nxt)
