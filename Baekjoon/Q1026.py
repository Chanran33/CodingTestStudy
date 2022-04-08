#그리디 실버4문제

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#B를 가장 큰 순서대로 정렬
B.sort(reverse=True)
#print(B)
#A를 가장 작은 순서대로 정렬
A.sort()
#print(A)

#B에 있는 수를 재배열하면 안된다 하더라도 덧셈인데.. 상관있나?
S=0
for i in range(N):
    S += A[i]*B[i]

print(S)

#맞았다!