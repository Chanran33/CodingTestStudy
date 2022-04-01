N = int(input())

coin = [500,100,50,10]

#거스름돈
result = 0

for i in coin:
    result += N//i
    N = N%i

print(result);