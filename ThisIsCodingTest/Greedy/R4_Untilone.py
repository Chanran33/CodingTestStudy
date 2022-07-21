N, K = map(int, input().split())

count = 0
while(True):
    if N==1:
        print(count)
        break

    if(N%K != 0 ):
        count += 1
        N -= 1
    else:
        count += 1
        N //= K

# n, k = map(int, input().split())

# result = 0

# while True:
#     target = (n//k)*k #k로 나누어떨어지는 수 한번에 찾기
#     result += (n - target) # 안나눠지는 값 한번에 더하기
#     print(n)
#     n = target
#     print(target, result)
#     #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     #K로 나누기
#     result += 1
#     n //=k

# #마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1) #n이 1보다 클때 연산을 한번에 진행
# print(result)