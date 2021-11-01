#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#리스트 접근자를 2중 이상 사용 가능
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a[1])
#res=[4, 5, 6]

#리스트 연산자
#덧셈 : 리스트 요소들을 결합
list_a = [1,2,3]
list_b = [4,5,6]

print(list_a+list_b)
#res = [1, 2, 3, 4, 5, 6]
print(list_a*3)
#res = [1, 2, 3, 1, 2, 3, 1, 2, 3]

# append -> 마지막에 요소추가
# insert -> 특정 부분에 요소 추가
# extend -> 기존 요소들 뒤에 새로운 리스트 요소 추가


# In[ ]:


#리스트 요소 제거하기
list_a = [0,1,2,3,4,5,6]

#인덱스로 제거 : del, pop

#del 키워드 -> 일반함수
del list_a[1]
print(list_a)

#pop 키워드 -> 객체 관련 매서드
list_a.pop(2)
print(list_a)

#값으로 제거하기

# remove -> 특정 값 제거
list_a = [0,1,2,3,4,5,6]
list_a.remove(2)
print(list_a)

# clear -> 모든 값 제거하기
list_a.clear()
print(list_a)


# In[ ]:


#list 요소 추가, 제거
list_a = [1,2,3]
list_b = [4,5,6]

#list 요소 추가
list_a.append("abcd")
print("list.append:",list_a)
list_a.insert(1,10)
print("list.insert:",list_a)

#list에 list 추가
list_a.extend(list_b)
print("list.extend:",list_a)

#list 요소 변경
list_a[3] = "변경"
print("list change [3]:",list_a)

#list 요소 제거
del list_a[1]
print("list del [1]:",list_a)

list_a.pop(2)
print("list pop [2]:",list_a)

list_a.remove("abcd")
print("list remove (abcd):",list_a)

list_a.clear()
print("list clear :",list_a)

#list 내부에 특정 요소가 있는지 확인
print(6 in list_b)
print(6 not in list_b)


# In[ ]:


# for문
# for 변수 in 반복자료 :
# <tab>처리 할 부분

#for문도 if문 처럼 들여쓰기 주의해야 처리가 제대로 이루어 진다

# range()
# range 함수에 인자가 1개 있으면 0부터 인자값까지 1씩 더하면서 진행
# range 함수에 인자가 2개 있으면 첫번째 숫자 부터 인자값까지 1씩 더하면서 진행
# range 함수에 인자가 3개 있으면 첫번째 숫자 부터 인자값까지 3번째 숫자 값을 더하면서 진행

for i in range(10):
# for문 시작 ------------------
    print(i)
# for문 종료 ------------------

for i in range(5,10):
# for문 시작 ------------------
    print(i)
# for문 종료 ------------------

for i in range(0,20,2):
# for문 시작 ------------------
    print(i)
# for문 종료 ------------------

#list를 반복자료로 사용
list_a = [100,30,421]
for i in list_a:
# for문 시작 ------------------
    print(i)
# for문 종료 ------------------

#문자열을 반복 자료로 사용
for i in "Hello world":
# for문 시작 ------------------
    print(i)
# for문 종료 ------------------



# In[ ]:


#p.159
#2중 리스트 요소 1개씩 출력하기

list_of_list = [[1,2,3],[4,5,6,7],[8,9]]

for y in list_of_list:
    for x in y:
        print(x)


# In[ ]:


#딕셔너리와 반복문
#딕셔너리는 키와 값이 있다 
# 키값은 반드시 문자열이거나 선언 된 변수를 써야 한다. 그냥 문자열을 써라

#선언 : 딕셔너리명 = { 키:값,키:값 ... 키:값 }
#출력 방법: 딕셔너리명["키"]
#           값이 여러개면 값을 리스트로 처리하면 된다.

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}

print("name:",dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:",dictionary["ingredient"])
print("origin:",dictionary["origin"])


#값 변경
dictionary["name"] = "8D 건조 망고",


# In[ ]:


#in 연산자
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}

key_input = input("찾으려는 키값 입력>")

if key_input in dictionary:
    print(dictionary[key_input])
else:
    print("키값이 존재하지 않습니다.")
    
value = dictionary.get(key_input)
print("입력한 키값:",key_input)
if value == None:
    print("키값이 존재하지 않습니다.")


# In[ ]:



dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀",
    "item" : {"key":"dict test", "value": "dict value"}
}

#for문장으로 값만 출력
for key in dictionary:
    print(dictionary[key])

print("dictionary type:" ,type(dictionary), "\name type:" , type(dictionary["name"]) , "\ningredient type:" , type(dictionary["ingredient"]))

#개별 데이터 출력
for key in dictionary:
    if (type(dictionary[key]) == list) or type(dictionary[key]) == dict:
        for data in dictionary[key]:
            print(data)
    else :
        print(dictionary[key])


# In[ ]:


#range(A) : 0~A까지 1씩 증가
#range(A,B) : A~B까지 1씩 증가
#range(A,B,C): A~B까지 C씩 증가

array = [273,45,103,54,101]
for i in range(len(array)):
    print("{}번째 데이터:{}".format(i,array[i]))

#뒤에서 부터 출력 하세요
for i in range(-1, (len(array) * -1) - 1, -1):
    print("{}번째 데이터:{}".format(i,array[i]))

# reversed() -> range 함수를 역순으로
for i in reversed(range(len(array))):
    print("{}번째 데이터:{}".format(i,array[i]))


# In[ ]:


# while 문. 무한 반복 위한 반복문

#무한 반복
#while True:
    
#
array = [273,45,103,54,101]

i = 0
while i < len(array):
    print("{}번째 데이터:{}".format(i,array[i]))
    i += 1
    
# 빈 리스트를 생성하고 키보드에서 자료 입력 받아 리스트 추가.
#입력값이 quit이면 입력 종료 후  list 값을 출력

input_list = []
input_data = ""

while input_data != "quit":
    input_data = input("문자열 입력>")
    input_list.append(input_data)
    i += 1

print(input_list)

#또는 이렇게도 쓴다
while True:
    input_data = input("문자열 입력>")
    if input_data.isdecimal():
        continue     #실행만 하지 않고 되돌림
    if input_data == "quit":
        break       #반복문 강제 종료
    input_list.append(input_data)
  

  



# In[ ]:


#부호를 입력받아 부호 입력 부분에 'q'를 입력하면 종료 되는 계산기

while True:
    operator = input("사칙연산 입력 (q 입력시 종료)>")
    if operator == 'q':
        break
    if operator not in "+-*/":
        continue
    
    num_data = input("두 수 입력>").split('.')
    
    if operator == '+':
        res = int(num_data[0]) + int(num_data[1])
    elif operator == '-':
        res = int(num_data[0]) - int(num_data[1])
    elif operator == '*':
        res = int(num_data[0]) * int(num_data[1])
    elif operator == '/':
        res = int(num_data[0]) / int(num_data[1])
        
    print("{}{}{}={}".format(num_data[0],operator,num_data[0],res))


# In[ ]:


# list에 적용 할 수 있는 기본 함수
# min()
# max()
# sum()
list_a = [34 , 54, 78, 100, 320, 43]
print("min:{}, max:{}, sum:{}".format(min(list_a),max(list_a),sum(list_a)))

# list 뒤집기 
# reversed()
print("org:{}, rev:{}".format(list_a, list(reversed(list_a))))

# 인덱스와 값 변환
# enumerate() 현재 인덱스가 몇번째인지 출력
for i, value in enumerate(list_a):
    print("{}번째 요소:{}".format(i, value))


# In[ ]:


dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}

for key, value in dictionary.items():
    print("{}:{}".format(key, value))
    if type(value) == dict:
        for key_1, vlaue in value.items():
            print(value)
    elif type(value) == list:
        for item in value:
            print(item)
    else:
        print(value)


# In[ ]:


#키보드에 입력을 받아서 리스트에 저장 ( q 입력하면 종료)
#검색 하고자 하는 이름 입력 받아 몇번째인지 출력
#enumerate 사용
namelist = []
nameindex = 0

while True:
    input_name = input("이름 입력>")
    if input_name == 'q':
        break
    namelist.append(input_name)
    
#이름 검색
input_name = input("검색 하려는 이름 입력>")
for i, value in enumerate(namelist):
    if value == input_name:
        print("{}(이)는 {}번째 있습니다.".format(input_name,nameindex))
        break
    else:
        print("{}(이)는 존재하지 않습니다.".format(input_name))
        break
        
#입력 된 이름의 갯수 만큼 점수를 입력하여 score 리스트에 저장
score_list = []

for index, name in enumerate(namelist):
    input_score = input(namelist[index] + "의 점수 입력:")
    score_list.append(input_score)
    
for index, name in enumerate(namelist):
    print("{}의 점수는 {} 입니다.".format(namelist[index],score_list[index]))


# In[ ]:


#리스트 내포
#리스트 내포란 list 인덱스 부분에 for문 같은 반복문 등을 사용하는 의미
# list = [(표현식) (반복문) (조건문)]
#--------------------------------------------------------
array = []
for i in range(0,20,2):
    array.append(i*i)
print(array)
#--------------------------------------------------------

array.clear()

# 리스트 내포
#--------------------------------------------------------
array = [ (i * i) for i in range(0,20,2) ]
print(array)
#--------------------------------------------------------

array.clear()


# if 조건문 삽입 가능
#--------------------------------------------------------
array = [ i for i in range(100) if i % 5 == 0 ]
print(array)
#--------------------------------------------------------

# 키보드에서 자료를 입력 받아 한 글자씩 리스트에 저장하고 문자만 리스트로 출력
list_input_data = list(input("input data>"))
str_list = [char for char in list_input_data if char.isalpha()]
print(str_list)


# In[ ]:


#문자열.join(문자열로 구성된 리스트)
# join함수 인자로 들어간 리스트 데이터를 join 앞 문자열로 머지하는 기능
list_data = ["1","2","3","4"]
string_data = ":".join(list_data)
print(string_data)

# 이터레이터
#
numbers = [1,2,3,4,5]
r_num = reversed(numbers)

#print(next(r_num))
#print(next(r_num))
print("1st")
for i in r_num:
    print(i)
    
print("2nd")
for i in r_num:
    print(i)


# In[ ]:


#함수

#def <함수명>(매개변수, 매개변수, ... ,매개변수)
#   처리내용

def print_function():
    print("function Test")
    return True

#매개변수 받기
def print_n_time(value, n):
    for i in range(n):
        print(value)
# 기본 매개변수
def  print_time(value, n = 3):
    for i in range(n):
        print(value)
    
#가변 매개변수
def print_val_time(n, * values):
    for i in range(n):
        for value in values:
            print(value)
    
#가변 매개변수 기본 매개변수
def print_basic_time(* values, n=3):
    for i in range(n):
        for value in values:
            print(value)
    
    
    
print_function()
print_n_time("test",3)
print_time("test")
print_val_time(2, "abcd", "test", 123)
print_basic_time("abcd", "test", 123)


# In[ ]:


#키보드 입력 받는 함수, 숫자와 부호를 받아서 리스트로 변환

def input_function():
    input_data = input("입력>").split()
    return input_data
    
def sum_function(num1,num2):
    return num1+num2

def sub_function(num1,num2):
    return num1-num2
    
res = 0    
while True:
    list_data = input_function()
    if 'q' in list_data:
        break
        
    if list_data[1] == '+':
        res = sum_function(int(list_data[0]),int(list_data[2]))
    elif list_data[1] == '-':
        res = sub_function(int(list_data[0]),int(list_data[2]))
    
    print("{}{}{}={}".format(list_data[0],list_data[1],list_data[2],res))
    
    

