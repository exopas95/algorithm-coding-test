"""
[제목]
- 무지의 먹방 라이브

[입력 조건]
- food_times는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열이다.
- K는 방송이 중단된 시간을 나타낸다.
- 만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.
- 먹방을 시작한 지 K초 후에 방송이 중지되었을 때, 다음 번 먹어야 하는 음식의 번호를 출력하라.

[출력 조건]
- 음식의 번호를 출력합니다.
"""


# %%
def solution(food_times, k):
    while k > 0:
        for i in range(0, len(food_times)):
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1

            if k == 0:
                result = (i + 1) % len(food_times) + 1
                print(result)


solution([3, 1, 2], 5)
