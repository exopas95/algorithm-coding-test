'''
[제목]
- 왕실의 나이트

[입력 조건]
- 첫째 줄에 8 * 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
- 입력문자는 a1처럼 열과 행으로 이뤄진다.

[출력 조건]
- 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
'''

# %%
x_label = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

location = input()
location_x, location_y = location[0], int(location[1])
location_x = x_label[location_x]

movements = [(1, -2), (1, 2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, 1), (-2, -1)]
count = 0
for move in movements:
    x = location_x + move[0]
    y = location_y + move[1]

    if x * y > 0:
        count += 1
print(count)


# %%
