 # 알고리즘 코딩 테스트 준비 - Python

나동빈 저자의 "이것이 취업을 위한 코딩 테스트다"를 기반으로 작성된 문서입니다. 알고리즘에 대한 기본적인 설명은 위 책을 기반으로 기술되었습니다. 

 ## 01. 그리디
단순하지만 강력한 문제 해결 방법으로 어떤 문제가 있을 떄 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘이다. 여기서 그리디 즉, 탐욕이란 "현재 상황에서 지금 당장 좋은 것만 고르는 방법"을 의미한다.

그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구하며 현재 상황에서 가장 좋아보이는 것만을 선택해도 문제를 풀 수 있는지를 파악할 수 있어야 한다. 거스름돈 문제가 대표적인 그리디 문제이다.

 ## 02. 구현
 코딩테스트에서 구현이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다. 어떤 문제를 풀든 간에 소스코드를 작성하는 과정은 필수이므로 구현 문제 유형은 모든 범위의 코딩 테스트 문제 유형을 포함하는 개념이다.
 
 그렇다면 어떤 문제가 구현하기 어려운 문제일까? 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제, 특정 소수점 자리까지 출력해야 하는 문제 ,문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트에 넣어서 파싱을 해야하는 문제 등이 까다로운 구현 유형의 문제이다. 대체로 사소한 조건 설정이 많은 문제일수록 코드로 구현하기가 까다롭다.
 
 이 책에서 완전탐색과 시뮬레이션 유형을 모두 '구현'유형으로 묶어서 다루고 있다.
 - 완전탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
 - 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야하는 문제 유형
 
 ## 03. DFS/BFS
 DFS/BFS에 앞서서 기초적인 자료구조 스택과 큐, 그리고 재귀 함수에 대해서 알아봐야 한다.
 ### 탐색
 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
 ### 자료구조
 데이터를 표현하고 관리하고 처리하기 위한 구조로 그중 스택과 큐는 자료구조의 기초개념으로 다음 **삽입(Push)**, **삭제(Pop)**으로 구성된다.
 ### 스택 (Stack)
 박스 쌓기에 비유할 수 있으며, 선입후출 또는 후입선출 구조라고 한다. 예를 들어 앞에서부터 a-b-c 순서로 입력이 됐다면 출력의 순서는 c-b-a의 순서이다. 파이썬에서는 스택을 위해서 별도의 모듈이 필요하지 않는다. 이미 주어진 append()와 pop() 매서드 만으로 스택을 구현할 수 있다.
 ### 큐 (Queue)
 대기 줄에 비유할 수 있으며, 선입선출 구조라고 한다. 예를 들어 a-b-c- 순서로 입력이 됐다면 출력의 순서 또한 a-b-c 이다. 파이썬에서 큐를 사용하기 위해서는 collections 모듈에서 제공하는 deque 자료구조를 활용하자. deque는 스택과 큐의 장점을 모두채택한 것인데 데이터를 넣고 뺴는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.
 ### 재귀함수
 자기 자신을 다시 호출하는 함수로 종료 조건을 꼭 명시해줘야 한다. 재귀함수는 수학에서의 점화식을 그대로 표현한 형식이기 때문에 반복문에 비해서 더 간단하다. 
   - n이 0 혹은 1일때: factorial(n) = 1
   - n이 1 보다 클 때: factorial(n) = n * factorial(n - 1)
 ### 그래프
 노드와 엣지로 구조를 표현하는 방법
   - **인접 행렬 방식**: 2차원 행렬에 각 노드가 연결된 형태를 기록하는 방식
   - **인접 리스트 방식**: 연결된 노드에 대한 정보를 차례대로 연결하여 리스트에 기록하는 방식
   - **차이**: 메모리 측면에서 인접행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다. 반면 인접 리스트는 연결된 정보만을 저장하기에 효율적이다. 하지만 인접 리스트 방식은 특정한 두 노드가 연결되어 있는지에 대한 정보 하나씩 확인해야 되기 때문에 얻는 속도가 느리다. 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.  
 ### DFS(Depth First Search)
 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 방법이다.  
   - 스택의 자료구조를 사용한다.
 #### 동작과정
 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
 3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.
```python
# DFS 메서드 정리
def dfs(grapyh, v, visited):
    # 현재 노드를 방문 처리
    visitied[v] = True
  
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visitied[i]:
            dfs(graph, i, visited)
```
 ### BFS(Breadth First Search)
 너비 우선 탐색이라고 부르며, 가까운 노드부터 탐색하는 알고리즘이다.
   - 큐 자료구조를 사용한다.
 #### 동작과정
 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
 ```python
 # BFS 메서드 정리
 def bfs(graph, start, visitied):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visitied[start] = True

    # 큐가 빌 때가지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visitied[i]:
            queue.append(i)
            visitied[i] = True
 ```
 ## 04. 정렬
 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. 정렬 알고리즘은 이진 탐색의 전처리 과정으로 내림차순, 혹은 오름차순으로 정렬을 해야 이진 탐색을 적용할 수 있기 때문에 정렬 알고리즘을 잘 아는 것은 매우 중요하다. 여기서는 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬과 함께 파이썬에서 정렬에 어떤 라이브러리를 사용해야하는 지를 다룬다.
 ### 선택 정렬
 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복**하는 정렬로 '매번 가장 작은 것을 선택'한다는 의미에서 선택 정렬 알고리즘이라고 한다.
 ```Python
for i in range(len(array)):
    min_index = i

    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            
    array[i], array[min_index] = array[min_index], array[i]  # 파이썬은 이런 식으로 Swap이 가능
 ```
 ### 삽입 정렬
 ### 퀵 정렬
 ### 계수 정렬
 ## 05. 이진 탐색
 ## 06. 다이나믹 프로그래밍
 ## 07. 최단 경로
 ## 08. 그래프 이론
