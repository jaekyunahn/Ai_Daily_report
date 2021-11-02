#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 재귀함수

# 재귀 함수란, 자기 자신을 호출 하는 함수로  자료를 반복적으로 사용할때 유용

# 재귀함수로 factorial함수 구현하기

# f(4) = 4 * f(3)
#      = 4 * 3 * f(2)
#         . . .
#      = 4 * 3 * 2 * 1

def factorial(number):
#
    if number == 1:
        return 1
    else :
        res = number * factorial(number - 1)
        return res
#
    
res = factorial(5)
print("!{} = {}".format(5,res))


# In[ ]:


# fibonacci 수열 구현하기

def fibonacci(number):
#
    global global_valiable_count
    global_valiable_count += 1
    if number == 1:
        return 1
    if number == 2:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)
#

global_valiable_count = 0
fibonacci(35)
print("fibonacci count:{}".format(global_valiable_count) )


# In[ ]:


dist_data = {
    1:1,
    2:2
}

def fibonacci_m(number):
#    
    global global_valiable_count
    global_valiable_count += 1
    
    if number in dist_data:
        return dist_data[number]
    else :
        output = fibonacci_m(number-1)+fibonacci_m(number-2)
        dist_data[number] = output
        return output
#    

global_valiable_count = 0
fibonacci_m(35)
print("fibonacci count:{}".format(global_valiable_count) )


# In[ ]:


#튜플
#함수와 함께 사용하는데 리스트와 비슷 하지만 요소 변경이 불가
#괄호로 묶기도, 없는것도 있다
# 튜플명 = (요소,요소, ... ,요소)

tuple_test = (1,2,3,4)
print("tuple_test={}".format(tuple_test))

a,b,c = 10,20,30
print("tuple_test=> a={} , b={}, c={}".format(a,b,c))

#함수 리턴 사용도 가능
def tuple_test_function():
    return (10,20)
print("tuple_test_function={}".format(tuple_test_function()))

#튜플 데이터 스왑
a,b = 10,20
a,b = b,a

print("swap > a={}, b={}".format(a,b))


# In[ ]:


for index, data in enumerate([1,2,3,4]):
    print("{}:{}".format(index, data))


# In[ ]:


#람다
#매개 변수로 함수를 전달 하기 위해 함수를 간단하고 쉽게 선언 하는 방법

def power(x):
    return x*x

def under3(x):
    return x<3

print("map(): ", list(map(power,[1,2,3,4,5])))
print("filter(): ", list(filter(under3,[1,2,3,4,5])))


# In[ ]:


a_power = lambda x : x*x
a_under3 = lambda x : x < 3

print("map(): ", list(map(power,[1,2,3,4,5])))
print("filter(): ", list(filter(under3,[1,2,3,4,5])))


# In[ ]:


#파일 처리
# 파일 오브젝트 생성
# 변수명 = open(<경로>,<옵션>)
# 파일 읽거나 쓰기
# 변수명.write() 또는 변수명.read()
# 파일 변경 사항 저장 하려면 close()함수 사용
# 변수명.close()

# open 옵션
# w: 생성 할 때마다 기존 파일 엎고 새로 만들기
# r: 존재하는 파일 읽기 모드
# a : 뒤에 이어서 쓰기
file = open("./test.txt", "w")
file.write("Hello File Test")
file.close()

file = open("./test.txt", "r")
read_buffer = file.read()
print(read_buffer)
file.close()

#파일오브젝트.seek(n)
# ->n번째 위치로 파일 포인터 이동


# In[ ]:


#제너레이터
#제너레이터 함수는 쌩으로는 실행 되지 않는다
def g_func():
    print("test1")
    yield "yield test1"
    
    print("test2")
    yield "yield test2"
    
    print("test3")
    yield "yield test3"

func = g_func()

#제너레이터 사용하기 -> next(제너레이터 함수명)
#  yield까지 실행하고 yield 뒤에 나오는 자료를 return
print(next(func))
print(next(func))
print(next(func))


#오전 끝


# In[ ]:


#
print("::".join(["1","2","3","4","5","6"]))


# In[ ]:


number = list(range(1,10+1))

# 홀수만 출력
print(list(filter(lambda x : x % 2  == 1 ,number)))
      
# 3이상 7미만
print(list(filter(lambda x : x >= 3 and x < 7 ,number)) )      
  
# 제곱해서 50 미만 추출하기
print(list(filter(lambda x : (x * x)  < 50 ,number)))     


# In[ ]:


#에러
#대부분 오류는 구문 오류나 인덱싱 오류가 주로 나온다

#예외 처리 방법
# 조건문 처리
# try구문

#Try 구문 예시
#try + except
#try + except + else
#try + except + finally

#try + except
try:
    input_number = int(input("정수 입력>"))
except Exception as error_code:
    #Exception -> Error 메세지 출력
    print("Error:",error_code)
else:
    print("입력한 정수는 {}입니다.".format(input_number))
finally:
    print("finally구문 실행.")


# In[ ]:


# 파일 try.txt 을 읽기 모드로 오픈, Error 발생 시 a 모드로 오픈
#마지막에 close 종료

try:
    fp = open("./try.txt", "r")
except Exception as error_code:
    print("Error:",error_code)
    fp = open("./try.txt", "a")
    fp.write("Test")
else:
    print(fp.read())
finally:
    fp.close()


# In[ ]:


def serch_number(serch_number,numbers):
    try:
        print("{}는 {}에 있습니다.".format(serch_number,numbers.index(serch_number)))
    except:
        print("{}는 리스트에 없습니다.".format(serch_number) )
    finally:
        print("함수가 종료 되었습니다.")
    
        
numbers = [52,273,32,103,90,10,275]

serch_number(53,numbers)
serch_number(103,numbers)


# In[ ]:


numbers = [52,273,32,103,90,10,275]

try:
    input_number = int(input("정수 입력>"))
    print("{}는 {}번 위치에 있습니다.".format(input_number,numbers.index(serch_number) ))
except ValueError as error_code:
    print("정수를 입력해주세요:{}".format(error_code) )
except IndexError as error_code:
    print("범위를 벗어났습니다:{}".format(error_code))
except Exception as error_code:
    print("Error:",error_code)
    


# In[ ]:


# raise -> 강제로 종료 하는 구문

