N, M = map(int, input().split())

cards = []
row = []
for i in range(N):
    row = list(map(int,input().split()))
    row.sort()
    cards.append(row)

def findBigNum(cards,N):
    numMax = cards[0][0]
    for i in range(N):
        if (cards[i][0] > numMax):
            numMax=cards[i][0]
            # print(cards[i][0])
    return numMax   

print(findBigNum(cards,N))

#아이디어: 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것
#min(), max()함수를 이용해서 풀 수도 있다.