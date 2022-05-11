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