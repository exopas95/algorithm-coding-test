'''
[제목]
- 떡볶이 떡 만들기

[내용]
- 떡볶이 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
- 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
- 손님이 왔을 ㄸ래 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

[입력 조건]
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필용한 양만큼 떡을 사갈 수 있다.
- 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

[출력 조건]
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''
# %%
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None


N = input()
nList = list(map(int, input().split()))
nList = sorted(nList)
M = input()
mList = list(map(int, input().split()))

result = []
for num in mList:
    search_result = binary_search(nList, num, 0, len(nList) - 1)

    if search_result == None:
        result.append('no')

    else:
        result.append('yes')

print(result)

# %%
import numpy as np
from sklearn.datasets import make_friedman1

N, M = list(map(int, input().split()))
ddeok_list = np.array(list(map(int, input().split())))

start = 0
end = max(ddeok_list)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    temp = ddeok_list - mid
    total = sum(np.where(temp < 0, 0, temp))

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
# %%
