N = int(input())
timeP = list(map(int, input().split()))
timeP.sort()
#print(timeP)

#오름차순으로 배열 후 더하는 것이 시간의 최솟값
result = timeP[0]
next = timeP[0]
for i in range(1,N):
    next += timeP[i]
    result += next

print(result)