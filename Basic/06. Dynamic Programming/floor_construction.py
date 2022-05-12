'''
[제목]
- 바닥 공사

[내용]
- 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
- 이 얇은 바닥을 1 * 2의 덮개, 2 * 1의 더팩, 2 * 2의 덮개를 이용해 채우려고 한다.
- 이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하라

[입력 조건]
- 첫째 줄에 N이 주어진다. (1 <= N <= 1,000)

[출력 조건]
- 첫째 줄에 2 * N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.
'''
# %%
n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
# %%