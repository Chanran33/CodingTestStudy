N, M = map(int, input().split())

Meats=[]
sum = 0
for i in range(N):
    weight, price = map(int, input().split())
    sum += weight
    Meats.append([sum, price])
Meats.sort(reverse=True)
# print(Meats)

pin = 0
for i in range(N):
    if M <= Meats[i][0]:
        pin += i
    else:
        break

if pin >=0 and pin <=N-1:
    print(Meats[pin][1])
else:
    print(-1)
    
