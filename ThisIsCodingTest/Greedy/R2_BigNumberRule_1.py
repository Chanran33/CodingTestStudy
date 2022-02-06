#실전문제2) 큰 수의 법칙

#N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[N-1] #가장 큰 수
second = data[N-2] #두번째로 큰 수

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)