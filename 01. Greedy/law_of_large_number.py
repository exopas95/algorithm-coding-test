'''
[제목]
- 큰 수의 법칙

[입력 조건]
- 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분된다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

[출력 조건]
- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
- 동빈이의 큰 수의 법칙: 주어진 수를 M번 더하여 가장 큰수를 만드는데 특정 인덱스가 연속해서 K번을 초과해서 더할 수 없다.
'''

# %%
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

first = max(data)
data.pop(-1)
second = max(data)

first_iter = int(m / (k + 1)) * k + (m % (k + 1))
second_iter = m - first_iter

result = first * first_iter + second * second_iter
print(result)

# %%
