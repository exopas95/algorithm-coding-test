"""
[제목]
- 만들 수 없는 금액

[입력 조건]
- 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어진다.
- 둘째 줄에는 각 동전의 화폐단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 이때 각 화폐 단위는 1,000,000 이하의 자연수이다.
- 이때 주어진 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 구하라.

[출력 조건]
- 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력한다.
"""
from itertools import combinations
import numpy as np

N = 5
List = [3, 2, 1, 1, 7]

possible_list = []

for i in range(0, len(List)):
    combination = list(combinations(List, i))
    possible_list += [sum(t) for t in combination]

result = sorted(set(possible_list))

for i in range(0, max(result) + 2):
    if i not in result:
        print(i)
        break

