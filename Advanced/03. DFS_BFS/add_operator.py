"""
[제목]
- 연산자 끼워 넣기

[내용]
- N개로 이루어진 수열 A1, A2, ... , An과 숫자 사이에 끼어넣을 수 있는 N-1 개의 연산자가 주어진다.
- 연산자는 -, +, /, * 로만 이루어져 있다.
- 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만든다고 했을 때 최댓값과 최솟값을 구하여라.
- 이때 나눗셈은 정수 나눗셈으로 몫만 취하며, 음수를 양수로 나눌 때에는 양수로 바꾼 뒤 몫을 취한고 그 몫을 음수로 바꾼다.

[입력 조건]
- 첫째 줄에 수의 개수 N이 주어진다.
- 둘째 줄에는 A1, A2, ..., An이 주어진다.
- 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수이다.

[출력 조건]
- 첫째 줄에 만들 수 있는 식의 결과의 최댓값을 출력한다.
- 둘째 줄에는 최솟값을 출력한다.
- 최댓값과 최솟값이 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
- 또한 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
"""
# %%
from itertools import permutations


def plus(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a < 0 and b > 0:
        return (abs(a) // b) * -1
    else:
        return a // b


n = int(input())
data = list(map(int, input().split()))
numbers = list(map(int, input().split()))
operators = []

for i in range(len(numbers)):
    for j in range(numbers[i]):
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        else:
            operators.append('/')

candidates = []
for i in permutations(operators, n - 1):
    candidates.append(i)

n_max = -1000000000
n_min = 1000000000
result = 0

for i in range(len(candidates)):
    for j in range(len(candidates[i])):
        a = data[j] if j == 0 else result
        b = data[j + 1]
        o = candidates[i][j]

        if o == '+':
            result = plus(a, b)
        elif o == '-':
            result = subtract(a, b)
        elif o == '*':
            result = multiply(a, b)
        else:
            result = divide(a, b)

    if result > n_max:
        n_max = result

    if result < n_min:
        n_min = result

print(n_max)
print(n_min)
