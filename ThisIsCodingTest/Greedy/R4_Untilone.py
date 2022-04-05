N, K = map(int, input().split())

count = 0
while(True):
    if N==1:
        print(count)
        break;

    if(N%K != 0 ):
        count += 1
        N -= 1
    else:
        count += 1
        N //= K

#책보다 더 쉽게 푼 것 같은 느낌이든다(?)