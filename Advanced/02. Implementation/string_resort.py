"""
[제목]
- 문자열 재정렬

[내용]
- 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤로 모든 숫자를 더한 값을 이어서 출력한다.

[입력 조건]
- 첫째 줄에 하나의 문자열 S가 주어진다.

[출력 조건]
- 첫째 줄에 문제에서 요구하는 정답을 출력한다.
"""

import re

code = "K1KA5CB7"

digit = str(sum([int(s) for s in re.findall(r'\d+', code)]))
alphabet = [s for s in re.findall(r'[A-Z]', code)]

result = ''.join((sorted(alphabet))) + digit
print(result)
