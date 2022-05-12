"""
[제목]
- 모험가 길드

[내용]
- 모험가 N명이 있다.
- 공포도가 X인 모험가는 반드시 X이상으로 구성된 모험가 그룹에 참여해야 여행을 떠날 수 있다.
- 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.
- 몇 명의 모험가는 마을에 남아 있어도 되기에 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

[입력 조건]
- 첫째 줄에 모험가의 수 N이 주어진다.
- 둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분된다.

[출력 조건]
- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.
"""

# %%
N = int(input())
X_list = [int(X) for X in input().split(' ')]
result = 0

while True:
    chick = max(X_list)
    result += 1

    for _ in range(0, chick):
        X_list.remove(max(X_list))

    if len(X_list) <= 0:
        break

print(result)
