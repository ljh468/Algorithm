# 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는방법
# 코딩테스트에서는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제됨

# 예제 00
# 당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 존재함
# 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하시오
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수 입니다.

# 최적의 해를 빠르게 구하기 위해서는 가장 큰화폐 단위부터 돈을 거슬러 주면 됨
# N원을 거슬러 줘야 할때, 가장 먼저 500원으로 거술러 줄 수 있을 만큼 거슬러 주고 100, 50, 10 차례대로 거슬러 주면 됨

# N = 1260일때
# 가장 큰 화폐 단위부터 돈을 거술러 주는 것이 최적의 해를 보장하는 이유는?
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문

n = 1260
count = 0
coins = [500, 100, 50, 10]
for coin in coins:
    count += (n // coin)
    n %= coin
print(count)

print("#######################################")
## 예제 01
# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 함
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있음
# 1. N에서 1을 뺌, 2. N을 K로 나눔
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오

# 입력조건 : 첫째줄에는 N(1<=N<=100000)과 K(2<=K<=100000)가 공백을 기준으로 하여 각각 자연수로 주어짐
# 출력조건 : 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력

# 주어진 N에 대하여 최대한 많이 나누기를 수행해야함
# N의 값을 줄일 때 2이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있음

# 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?

# 입력예시 : N=25, K=3 , 출력예시 : 6

n, k = map(int, input().split())
result = 0 # 계산 횟수

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k: # 더이상 나눌수 없을때 반복문 탈출
        break
    # k로 나누기
    result += 1
    n = n // k

# 마지막 남은수에서 1씩 빼기
result += (n-1)
print(result)

print("#######################################")

## 예제 02
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은
# '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, +보다 x를 먼저 계산하는 일반적인 방식과 달리, 모든 연산은 왼쪽에서부터 순서대로 진행

# 입력조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어짐
# 출력조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력

# 대부분 + 보다는 * 가 값을 더 크게 만듬
# 다만 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적임
# 따라서 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하면 정답

# 입력예시 : 02984 , 출력예시 : 576

data = input()
result = int(data[0]) # 첫번째 숫자 넣기

for i in range(1, len(data)):
    # 1,2,3,4 까지
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

print("#######################################")
## 예제 03
# 한 마을에 모험가가 N명 있음, 모험가 길드에서는 N명의 모험가를 대상으로 '공포도' 를 측정했는데,
# '공포도' 가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어짐
# 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야만 여행을 떠날수있음
# N명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오

# 입력조건 : 첫째 줄에 모험가의 수 N이 주어짐, 각 모험가의 공포도의 값은 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분
# 출력조건 : 여행을 떠날 수 있는 그룹 수의 최댓값을 출력

# 입력예시 : 5
# 입력예시 : 2 3 1 2 2
# 출력예시 : 2
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data)

result = 0 # 총그룹의 수
count = 0 # 그룹에 포함된 모험가의 수
for i in data:
    count += 1 # 모험가의 수 추가
    if count >= i:
        result += 1
        count = 0
    else:
        continue
print(result)
