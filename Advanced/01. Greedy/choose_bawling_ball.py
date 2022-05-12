"""
[제목]
- 볼링공 고르기

[입력 조건]
- 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어진다.
- 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어진다.
- 이때 두 사람이 고를 수 있는 볼링공 번호의 조합의 경우의 수를 구하여라.

[출력 조건]
- 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력한다.
"""

# %%
N, M = map(int, input().split(' '))
balls = list(map(int, input().split(' ')))

count = 0
for i in range(0, len(balls)):
    for j in range(i+1, len(balls)):
        if balls[i] != balls[j]:
            count += 1

print(count)
