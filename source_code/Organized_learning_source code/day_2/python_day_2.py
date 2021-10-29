#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#복습: 키보드로 부터 입력을 받아 문자열을 출력, 길이를 구하세여
input_string = input ("문자열 입력>")
print("입력한 문자열:", input_string , " \n문자열 길이:", len(input_string))


# In[ ]:


#format 함수. 숫자 데이터를 문자열로 변환
# 대괄호를 입력 한 만큼 format 함수 아규먼트를 주면 순차적으로 적재 된다.
a = 10
b = 20
print("{} + {} = {}".format(a,b,a+b))

print("입력 받은 문자:{}\n입력받은 문자 길이:{}".format(input_string,len(input_string)))


# In[ ]:


# 정수 자리수 지정하기

#특정 칸에 출력하기
print("{:5d}".format(1000))
#특정 칸에 출력하되 앞부분 0으로 채우기
print("{:03d}".format(32))

print("{:d}".format(100))
print("{:1d}".format(100))
print("{:5d}".format(100))
print("{:10d}".format(100))
print("{:010d}".format(100))
print("{:010d}".format(-100))


# In[ ]:


#부호 붙이기

#부호 강제로 표기하기
print("{:+d}".format(16))
print("{:+d}".format(-16))
#부호자리 비워두기. 양수는 +가 출력 되지 x
print("{: d}".format(16))
print("{: d}".format(-16))


# In[ ]:


#조합하기
print("{:+5d}".format(52))
print("{:+5d}".format(-52))

# 0번째 자리에 기호 박기
print("{:=+5d}".format(52))
print("{:=+5d}".format(-52))

# 0번째 자리에 기호 박고 빈칸에 0 채워 넣기
print("{:+05d}".format(52))
print("{:+05d}".format(-52))


# In[ ]:


#소수점 출력 
num_float = 3.1415

print("{:f}".format(num_float))

print("{:15f}".format(num_float))
print("{:+15f}".format(num_float))
print("{:+015f}".format(num_float))

#소수점 미만 자리수 카운트 지정, 정수.소수
print("{:15.3f}".format(num_float))

#의미 없는 소수점 제거
print("{:g}".format(num_float))


# In[ ]:


#문자열 함수

string_data = " Show Me The Money "

#upper->모든 알파벳을 대문자로 전환
print("#",string_data.upper(),"#")

#upper->모든 알파벳을 소문자로 전환
print("#",string_data.lower(),"#")

#strip->양쪽 공백 제거
print("#",string_data.strip(),"#")

#lstrip->왼쪽 공백 제거
print("#",string_data.lstrip(),"#")

#rstrip->오른쪽 공백 제거
print("#",string_data.rstrip(),"#")

#조합하기. 파이썬은 객체지향이라 연달아 붙이기가 가능하다
#소문자로 바꾸고 양쪽 공백 제거
print("#",string_data.lower().strip(),"#")


# In[ ]:


#문자열 구성 파악 하기. is함수명(), 반환은 bool type data

print("ShowMeTheMoney1000".isalnum())
print("10".isdigit())

print("import10".isdecimal())


# In[ ]:


#문자열 찾기

string_data = "Show Me The Money The"

#왼쪽에서 부터 찾기. 리턴 값은 배열 인덱스
print(string_data.find("The"))

#"Show Me The Money The"
#         T

#오른쪽에서 부터 찾기
print(string_data.rfind("The"))

#"Show Me The Money The"
#                   T

#최초 검색 된 "the" 뒤 문자열 부터 모두 출력
print(string_data[ (string_data.find("The")) : ])


# In[ ]:


#키보드에 문자열 입력 받아서 처음 공백나오는 부분까지만 문자열 출력
# find에 아규먼트 아무 것도 안주면 공백으로 간주
input_string = input("문자열 입력>")
print(input_string[:input_string.find()])


# In[3]:


#split-> 문자열 자르기, list 형식으로 반환

#공백 단위 분리
string_data = "10 20 30 AB CD"
temp = string_data.split()
print(temp)

#콤마 단위 분ㄹ
string_data = "50,60,70,EF,GH"
temp = string_data.split(',')
print(temp)


#키보드 입렵 받아 공백으로 분리하고 두번째 자료를 출력
input_data = input("키보드 입력>")
temp = input_data.split()
print(temp[1])


# In[6]:


#Bool 연산

#and or not, < , = , > == ...
a = 10
b = 20

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print(a==10 and b==20)
print(a!=10 and b==20)
print(a==10 and b!=20)
print(a!=10 and b!=20)
print(a==10 or b==20)
print(a!=10 or b==20)
print(a==10 or b!=20)
print(a!=10 or b!=20)
print(not(a!=10 or b!=20))


# In[8]:


#if 조건문

if True:
    print("if true 문장 실행")
    
if False:
    print("if false 문장 실행")
    
    
    
    
input_data = input("정수입력>")
#숫자인지 확인
if input_data.isdecimal() :
    if 10 > int(input_data) :
        print("10보다 작은 수 입니다.")


# In[12]:


#숫자를 입력 받아 실수로 변환, 0보다 크면 양수 0보다 작으면 음수, 0이면 제로라고 출력

input_num = input("숫자 입력>")
if float(input_num) > 0 :
    print("양수")
elif float(input_num) < 0 :
    print("음수")
else:
    print("0")


# In[15]:


#날짜/시간 관련 함수 사용하기 위한 모듈 가져오기
import datetime

get_datetime = datetime.datetime.now()

print("현재 {}년 {}월 {}일 {}시 {}분 {}초 입니다."
    .format
    (
        get_datetime.year, 
        get_datetime.month, 
        get_datetime.day, 
        get_datetime.hour,
        get_datetime.minute,
        get_datetime.second
    )
)


# In[18]:


#정수입력을 받아서 홀 짝 구분
get_intger = input("정수입력>")
last_char = int(get_intger[-1])

iflast_char == 0 orlast_char == 2 orlast_char == 4 orlast_char == 6 orlast_char == 8 :
    print("입력한 정수는 짝수 입니다.")
else:
    print("입력한 정수는 홀수 입니다.")


# In[20]:


#정수입력을 받아서 홀 짝 구분
get_intger = input("정수입력>")
last_char = int(get_intger[-1])

# 나머지를 통한 홀짝 구분
if (last_char % 2 )== 0 :
    print("입력한 정수는 짝수 입니다.")
else:
    print("입력한 정수는 홀수 입니다.")

# in을 이용하여 구분
if last_char in "02468":
    print("입력한 정수는 짝수 입니다.")
else:
    print("입력한 정수는 홀수 입니다.")


# In[25]:


# 두개의 숫자를 입력 받아서 작은 수 부터 출력
# 작은 수와 큰 수가 2의 배수인지 3의 배수인지 확인

number_string = input("숫자 두개 입력>")

temp = number_string.split()

#print("{}와{}를 입력함".format(temp[0],temp[1]))

num_1 = int(temp[0])
num_2 = int(temp[1])

if num_1 > num_2:
    print("{}와{}를 입력함".format(num_2,num_1)) 
elif num_1 < num_2:
    print("{}와{}를 입력함".format(num_1,num_2))

if ( num_1 % 3 ) == 0:
    print("{}는 3의 배수 O".format(num_1))
else:
    print("{}는 3의 배수 X".format(num_1))
    
if ( num_2 % 3 ) == 0:
    print("{}는 3의 배수 O".format(num_2))
else:
    print("{}는 3의 배수 X".format(num_2))    
    


# In[29]:


# 점수 입력하여 ~90->A , 80 -> B , 70 -> C , 그외 D

input_data = int(input("점수 입력>"))

if input_data >= 90 :
    print("점수:A")
elif (input_data >= 80) and (input_data < 90) :
    print("점수:B")
elif (input_data >= 70) and (input_data < 80) :
    print("점수:C")
else :
    print("점수:D")


# In[34]:


#날짜와 날짜 함수에서 월을 추출하여 현재 월의 계절 추출

import datetime as dt

get_date = dt.datetime.now()
input_data = int(get_date.month)

print("현재는 {}월 입니다.".format(input_data))

if (input_data >= 1) and (input_data <= 3) :
    print("봄")
elif (input_data >= 4) and (input_data <= 6) :
    print("여름")
elif (input_data >= 7) and (input_data <= 9) :
    print("가을")
else :
    print("겨울")
    

    


# In[41]:


#숫자 부호를 입력 받아 계산하는 프로그램
# 예 ) 10 + 20 -> 덧셈

input_string = input("식 입력")

temp = input_string.split()
#print(temp)

# 1->덧셈 2 -> 뺄셈 , 3 -> 곱, 4 -> 나눗셈
cal_type = 0

num_1 = int(temp[0] )
num_2 = int(temp[2] )
res = 0

if temp[1] == '+':
    res = num_1 + num_2
elif temp[1] == '-':
    res = num_1 - num_2
elif temp[1] == '*':
    res = num_1 * num_2
elif temp[1] == '/':
    if num_2:
        res = num_1 / num_2
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("식이 틀림")
    
print("{} {} {} = {}".format(num_1,temp[1],num_2,res))


# In[50]:


#list append, insert
list_data_a = [1,2,3]
list_data_b = ["A","B","C"]

print("list_data_a + list_data_b=", list_data_a + list_data_b)
print("list_data_a * 3=", list_data_a  * 3)

list_data_c = list_data_a + list_data_b
      
print("list_data_a 개수:{}, list_data_b 개수:{}, list_data_c 개수:{}".
      format( 
          len(list_data_a), 
          len(list_data_b), 
          len(list_data_c) 
      )
)

list_data_a.append(list_data_b)
print(list_data_a[3][0])

list_data_a.insert(1,list_data_c )
print(list_data_a)


# In[63]:


# a_list = [ 1, 2, 3],  b_list = ["test", "abcd"]
a_list = [ 1, 2, 3]
b_list = ["test", "abcd"]

# a_list에 b_list를 '+'와 같은 개념으로 추가하세요
a_list.extend(b_list)
print(a_list, "\t",b_list)

# a_list에 b_list를 append로 추가하세요
a_list.append(b_list)
print(a_list, "\t",b_list)

# 추가된 a_list에서 "abcd" 를 출력 하세요 -> index 를 이용하여
print(a_list[-1][-1])

# b_list에서 "test" 앞에 "name"을 추가 하세요
b_list.insert(0,'name')
print(b_list)

# a_list의 두번째 요소를 'change'로 변경하세요
a_list[1] ='change'

# a_list와 b_list를 출력해 보세요
print("a : ", a_list,"\n","b : ", b_list)

