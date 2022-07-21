N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
for i in reversed(coins):
    if K>=i:
        point = K//i
        count += point
        K -= (i*point)

print(count)


"""
if K>i처리를 해줬을 때 틀렸습니다 라고 나옴.
"""