'''
큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때,
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
(단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 업는 것이 이 법칙의 특징이다.
'''

#배열의 크기 N, 더해지는 횟 수 M, K번 초과해서 연속으로 더할 수 없음.
N,M,K = map(int, input().split())
print(N,M,K)

numbers = list(map(int, input().split()))
#print(numbers)

#정렬하기
numbers.sort(reverse=True) #6 5 4 4 2

result = 0
repeat = M//(K+1)
plus = M%(K+1)

print(repeat,plus)

for i in range(repeat):
    for j in range(K):
        result += numbers[0]
    result += numbers[1]

result += (numbers[0]*plus)

print(result)