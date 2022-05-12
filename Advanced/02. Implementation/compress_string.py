"""
[제목]
- 문자열 압축
- 링크: https://programmers.co.kr/learn/courses/30/lessons/60057

[내용]
- 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 반환하라.

[입력 조건]
- 첫째 줄에 s가 주어진다.
- s의 길이는 1 이상 1,000 이하이다.
- s는 알파벳 소문자로만 이루어져 있다.

[출력 조건]
- 가장 짧은 단위를 출력하라.
"""

# s = list(input())
s = "ababcdcdababcdcd"
#
# length = len(s)
# result = []
#
# # 마디 자르기
# for i in range(0, length):
#     num = 2
#
#     j = 0
#     while length > j:
#         count = 1
#         for k in range(j + num, length, num):
#             A = s[j:j+num]
#             B = s[k:k+num]
#
#             if A == B:
#                 count += 1
#                 if k == length - num:
#             else:
#                 if count == 1:
#                     result.append(A)
#                 else:
#                     result.append(f"{count}{A}")
#                 j = k
#                 break
#
# print(result)

answer = len(s)
for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step]
    count = 1

    for j in range(step, len(s), step):
        if prev == s[j:j + step]:
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j + step]
            count = 1

    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))

print(answer)



