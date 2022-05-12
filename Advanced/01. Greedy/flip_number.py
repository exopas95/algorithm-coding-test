"""
[제목]
- 문자열 뒤집기

[내용]
- 0과 1로만 이루어진 문자열 S를 가지고 있다.
- 이 문자열 S에 있는 모든 숫자를 전부 같게 만드려고 한다.
- 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
- 예를 들어 S = 0001100일때 이를 뒤집으면 1110011이되고 4, 5번째 문자열을 뒤집으면 1111111이 된다.
- 하지만 처음부터 4번째부터 5번째까지 문자를 뒤집으면 한 번ㅇ에 0000000이 되어서 한 번만에 같은 숫자를 만들 수 있다.
- 이때 문자열 S가 주어졌을 때 행동의 최소 횟수를 출력하라.

[입력 조건]
- 첫째 줄에 0과 1로만 이루어진 문자열 S가 우저니다. S의 길이는 100만보다 작다.

[출력 조건]
- 첫째 줄에 해야 하는 행동의 횟수를 출력한다.
"""

# %%
S = map(int, list(input()))

flag = True
count_zero = 0
count_one = 0

for num in S:
    if num != 0 and flag is True:
        flag = False
        count_zero += 1
    elif num == 0 and flag is False:
        flag = True

for num in S:
    if num != 1 and flag is True:
        flag = False
        count_one += 1
    if num == 1 and flag is False:
        flag = True

result = count_one if count_one <= count_zero else count_zero
print(count_zero, count_one, result)


