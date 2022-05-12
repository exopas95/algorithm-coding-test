"""
[제목]
- 럭키 스트레이

[내용]
- N을 반으로 나눈 쪽의 왼쪽 자릿수의 합과 오른쪽 자리수의 합이 같은 경우 LUCKY를 출력한다.

[입력 조건]
- 첫째 줄에 정수 N이 주어진다.
- 단 정수 N의 자리수는 항상 짝수이다.

[출력 조건]
- 첫째 줄에 럭키 스트레이트를 상용할 수 있다면 "LUCKY"를, 없다면 "READY"를 출력한다.
"""

import numpy as np

N = np.array(list(map(int, input())))
mid = int(len(N) / 2)
left = N[:mid]
right = N[mid:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
