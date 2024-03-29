﻿import sys

print("#######################################")
# 1. 정수형
a = 1000
b = -7
c = 0
print(a,b,c)

print("#######################################")
# 2. 실수형
a = 157.93
b = -1837.2
# 소수부가 0일때 0을 생략
c1 = 5.
c2 = -.7
print(a,b,c1,c2)

# 지수표현방식
# 유효숫자 e 지수 = 유효숫자 * 10 지수

# 1,000,000,000
a = 1e9
print(a)
print(int(a))

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# 부정확한 실수형데이터를 처리하기위해서는 round()함수를 이용
a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)

# 나누기 연산자는 나눠진 결과를 실수형으로 반환
a = 5
b = 3
# 나누기연산자 /
print(a / b)
# 나머지 연산자 % (홀수인지 짝수인지 체크해야할때)
print(a % b)
# 몫 연산자 //
print(a // b)
# 거듭제곱 연산자 **
print(a ** b)

print("#######################################")
# 3. 리스트형
# 리스트는 대괄호([])안에 원소를 넣어 초기화함, 쉼표(,)로 원소를 구분함
# 리스트의 원소에 접근할때는 Index값을 괄호에 넣는다, Index는 0부터
a1 = list()
a2 = []
print(a1, a2)

# 직접 데이터를 넣어 초기화
a = [1,2,3,4,5,6,7,8,9]
print(a)

# 4번째 원소만 출력
print(a[3]) # -> 4

# 크기가 N이고, 모든값이 0인 1차원 리스트 초기화
n = 10
a = [0]* n
print(a) # -> [0,0,0,0,0,0,0,0,0,0]

print("#######################################")
# 3-1. 인덱싱
# 리스트의 특정한 원소에 접근하는것을 인덱싱이라고 함
# Python은 인덱스값을  양의정수, 음의정수, 모두 사용가능 (음의정수를 넣으면 거꾸로 탐색)
a = [1,2,3,4,5,6]
print(a[2]) # -> 3
print(a[-1]) # -> 6

# 4번째 원소값 변경
a[3] = 7
print(a) # -> [1,2,3,7,5,6]

print("#######################################")
# 3-2. 슬라이싱
# 연속적인 위치를 갖는 원소들을 가져와야 할때는 슬라이싱을 사용
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정
a = [1,2,3,4,5,6,7,8,9]

# 두번째 원소부터 4번째 원소까지
print(a[1:4])
# 슬라이싱의 마지막 입력 인덱스는 가져오지않음

print("#######################################")
# 3-3. 리스트 컴프리헨션
# 리스트 대괄호 안에 조건, 반복을 적용하여 초기화

# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)] # 반복문 먼저 넣어주고 담길변수 맨앞; range는 0~9까지 범위
print(array)

# 0부터 19까지의 수중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지 수들의 제곱값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# 리스트 컴프리헨션은 2차원리스트를 초기화할때 효과적!!
# N * M 크기의 2차원 리스트를 한번에 초기화 해야할때 매우 유용

#   좋은예 ) array = [[0]*M for_ in range(n)]
# 잘못된예 ) array = [[0]*M]*N
# 잘못된예처럼 그냥 N을 곱해주면 내부의 각리스트가 모두 같은 객체로 인식될수있다.

# N * M 크기의 2차원리스트 초기화
n = 4
m = 3
array = [[0]*m for _ in range(n)]
print(array)
array[1][1] = 5
print(array)

# 언더바 (_)는 반복을 하되 반복을 위한 변수의값을 무시하고자 할때 사용
# # 코드1) 1부터 9까지의 자연수를 더하기
summary = 0
for i in range(1,10):
    summary += i
print(summary)

# 코드2) Hello world를 5번 출력하기
for _ in range(5): # 5번 반복하게됨 0~4인덱스 만큼
    print("Hello world")

print("#######################################")
# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본리스트 : ", a)
# append() = 변수명.apped() # 리스트에 원소하나를 추가할때
a.append(2)
# sort() = 오름차순
a.sort()
# sort() = 변수명.sort(reverse=Ture) * 내림차순
a.sort(reverse=True)
# reverse() = 변수명.reverse() * 리스트에 원소의 순서를 거꾸로 넣음
a.reverse()
# count() = 변수명.count(특정값) * 리스트에서 특정값의 개수를 셈
a.count(3)
# remove() = 변수명.remove(특정값) * 원소가 여러개면 하나만 제거
a.remove(1)
# insert() = insert(삽입할위치 인덱스, 삽입할값) * 특정한 인덱스 위치에 원소 삽입
a.insert(2, 3)

# 리스트에서 특정값을 가지는 원소 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} # 집합자료형 (딕셔너리)
# remove_set에 포함되지 않는 값만을 저장
result = [i for i in a if i not in remove_set] # 3,5가 아닌값만
print(result)

print("#######################################")
# 4. 문자열 자료형
# 문자열 변수를 초기화할때는 큰따옴표(")나 작은따옴표(')를 이용함
# 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있음
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열변수에 덧셈(+)를 이용하면 문자열이 더해져서 연결됨
# 문자열을 곱하는 경우 값만큼 여러번 더해짐
# 문자열도 인덱싱과 슬라이싱을 이용할 수 있음 (다만, 특정 인덱스의 값을 변경은 안됨) # EX) a[2] = 'a' 안됨XX
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

print("#######################################")
# 4-1. 튜플 자료형
# 리스트와 유사하지만 한번 선언된 값을 변경할 수 없음
# 리스트는 대괄호[]를 이용하지만, 튜플은 소괄호()를 이용함
# 튜플은 리스트에 비해 상대적으로 공간 효율적임

a = (1,2,3,4,5,6,7,8,9)

# 4번째 원소만 출력
print(a[3])
# 2번째 원소부터 4번째 원소까지
print(a[1 : 4])

# 특정한 인덱스의 값을 바꾸지못함
a = (1,2,3,4)
print(a)

# 이거 안됨 XX
# a[2] = 7

# 튜플은 서로다른 성질의 데이터를 묶어서 관리해야할 때
# 최단경로 알고리즘에서는 (비용, 노드번호)의 형태로 튜플 자료형을 자주 사용함
# 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
# 튜플은 변경이 불가능하므로 리스트와 다르게 키값으로 사용될 수 있음
# 리스트보다 메모리를 효율적으로 사용해야 할 때

print("#######################################")
# 4-2. 사전자료형(Dictionary)
# 사전자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형
# 변경불가능한 자료형을 key로 사용
# 해시테이블을 이용하므로 데이터조회 및 수정에 있어서 O(1)의 시간에 처리할수 있음
data = dict() # 초기화
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data) # -> {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}

# 키 데이터를 뽑아서 리스트로 반환
Key_list = data.keys()
# 값데이터
value_list = data.values()
# 각 키에 따른 값을 하나씩 출력
for key in Key_list:
    print(data[key]) # ->Apple Banana Coconut

b = {'홍길동':97, '이순신':98}
print(b)
key_list = b.keys()
print(key_list) # -> dict_keys(['홍길동', '이순신']) -객체로 변환
key_list = list(b.keys())
print(key_list) # -> ['홍길동', '이순신'] -리스트자료형으로 형변환

print("#######################################")
# 4-3. 집합자료형 (Set)
# 원소의 중복을 허용하지않음
# 순서가 없음
# 데이터가 존재하는지, 아닌지 확인할때 쓰임
# 리스트 or 문자열을 이용해서 초기화함, set() 함수 이용
# 중괄호({})안에 각 원소를 콤마(,)를 기준으로 구분함, O(1)시간복잡도

# 집합자료형 초기화
data = set([1,1,2,3,4,4,5])
print(data)
# 집합자료형 초기화2
data = {1,1,2,3,4,4,5}
print(data)

# 집합자료형의 연산
# 합집합 : A or B , A | b는 안됨
# 교집합 : A and B , A & B 안됨
# 차집합 : A - B

data = set([1,2,3])
# 새로운원소 추가
data.add(4)
print(data) # -> {1,2,3,4}
# 새로운원소 여러개 추가
data.update([5,6])
print(data) # -> {1,2,3,4,5,6}
# 특정한 값을 갖는 원소 삭제
data.remove(3) # -> {1,2,3,4,5,6}
print(data)
## 사전자료형과 집합자료형의 특징
# 리스트나 튜플은 순서가 있기때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
# 사전자료형(Dictionary), 집합자료형(Set) 은 순서가 없기때문에 인덱싱 할수없음 X
# 사전의 Key or 집합의 원소를 이용해 O(1)시간복잡도로 조회

print("#######################################")
# 5. 기본입출력
# input()함수는 한 줄의 문자열을 입력 받는함수
# map()함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용
# list(map(int, input().split())) 공백으로 구분하여 정수형으로 바꾼뒤 리스트로 만듬

# 학생 성적 데이터를 내림차순으로 정렬
# 데이터 개수 입력
print("데이터개수를 입력하세요.")
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
print("공백을 기준으로 데이터를 입력하세요.")
data = list(map(int, input().split())) # <- 65,90,75,34,99
data.sort(reverse=True)
print(data) # -> {99, 90, 75, 65, 34}

# n, m, k를 공백을 기준으로 구분하여 입력
print("공백을 기준으로 3개의 데이터를 입력하세요.")
n, m, k = map(int, input().split())
print(n, m, k)

# 사용자로부터 입력을 최대한 빠르게 받아야 하는경우
print("sys.stdin.readline을 사용합니다.")
sys.stdin.readline().rstrip() # 엔터가 줄바꿈기호로 입력되므로 오른쪽 공백제거

# 파이썬의 기본 출력은 print(), 기본적으로 출력이후 줄바꿈을 수행 ( 원치않으면 'end'속성 이용 )
# 출력할 변수
a,b = 1,2
print(a,b)
print(7, end="")
print(8, end="") # -> 78

# 출력할변수
answer = 7
print("정답은 "+ str(answer) + "입니다.")

# F-string, 파이썬3.6부터 문자열 앞에 f를 붙여 간단히 정수와 문자열을 함께 넣을 수 있음
answer = 7
print(f"정답은 {answer} 입니다") # -> 정답은 7입니다.

##################################### ch5 까지 종료 ####################################