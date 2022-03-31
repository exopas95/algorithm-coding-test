"""
[제목]
- 팀 결성

[내용]
- 학생들에게 0번부터 N번까지의 번호를 부여했다.
- 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N + 1 개의 팀이 존재한다.
- 이때 선생님은 팀 합치기 연산과 같은 팀 여부 확인 연산을 사용할 수 있다.
- 팀 합치기 연산: 두 팀을 합치는 연산
- 팀 여부 확인 연산: 두 학생이 같은 팀에 속하는지 확인하는 연산
- 선생님이 M개의 연산을 수행할 수 있을 때, 같은 팀 여부 확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성하라.

[입력 조건]
- 첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산 개수다.
- 다음 M개의 줄에는 각각의 연산이 주어진다.
- 팀 합치기 연산은 0 a b 형태로 주어진다. a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
- 같은팀 여부 확인 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해있는지 확인하는 연산이다.

[출력 조건]
- 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES 또는 NO로 결과를 출력한다.
"""
# %%
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(0, n + 1):
    parent[i] = i

for i in range(m):
    method, a, b = map(int, input().split())
    if method == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
