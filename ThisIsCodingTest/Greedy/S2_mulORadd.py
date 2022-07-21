"""
아이디어 
주어진 문자열 앞에서부터 +와 x연산을 한후 더 큰 값이 나온걸 통과시킨다.
"""

S_input = input()
#문자를 입력받아 char하나를 int형으로 변환해 리스트에 넣어준다.
S = [int(i) for i in S_input]

result = S[0] #첫 비교대상은 첫번째 인자
for i in range(1,len(S)):
    if(result + S[i] <= result * S[i]):
        result *= S[i]
    else:
        result += S[i]

print(result)

"""
정답
"""
data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
 
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0'혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <=1 :
        result += num
    else:
        result += num

print(result)