N = int(input())
path = list(input().split())

x,y = 1,1

for i in path:
    if 'L':
        y-1
    elif 'R':
        y+1
    elif 'U':
        x-1
    elif 'D':
        x+1

print(x,y)