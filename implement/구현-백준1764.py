import sys
N,M = map(int,input().split())

# ##딕셔너리 이용
# dic = {}
# result = []
# count = 0
# for _ in range(N):
#     dic[str(sys.stdin.readline().strip())] = 1
# for _ in range(M):
#     name = str(sys.stdin.readline().strip())
#     if name in dic:
#         result.append(name)
#         count+=1
# result.sort()
# print(count)
# for i in range(count):
#     print(result[i])

#set함수를 사용 하여 풀 수도 있다.
set1 = set()
set2 = set()
for _ in range(N):
    set1.add(str(sys.stdin.readline().strip()))
for _ in range(M):
    set2.add(str(sys.stdin.readline().strip()))

set3 = set1 & set2
print(len(set3))
s3 = list(set3)
s3.sort()
for i in s3:
    print(i)