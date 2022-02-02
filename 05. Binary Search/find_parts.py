'''
[제목]
- 부품 찾기

[내용]
- 부품 N개가 있으며 각 부품은 정수 형태의 고유한 번호가 있다.
- M개의 종류의 부품을 대량으로 구매할 때 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
- 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하자.

[입력 조건]
- 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
- 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 1,000,000)
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

[출력 조건]
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
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