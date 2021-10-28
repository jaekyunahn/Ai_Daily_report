#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello Python")


# In[ ]:


a = 10
b = 20
a + b
# a + b


# mark 모드 입니다. 명령어는 m

# In[ ]:


#코드 모드 입니다. 명령어는 y


# In[ ]:


import keyword

print(keyword.kwlist)


# In[ ]:


#주석
'''주석
주석
주석
코드 여러줄 주석 칠때'''

# 여러줄 드래그 하고 ctrl + / (슬레시)하면 여러줄 주석 처리 되거나 주석 해제. 토글 기능

# 여러줄
# 주석
# 처리

10 + 20 #test 30


# In[ ]:


# 하나만 출력합니다.
print("#하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러개를 출력합니다.
print("# 여러개를 출력합니다.")
print(10,20,30,40,50)
print("안녕하세요","저의","이름은","안재균 입니다.")
print()

# 아무 것도 입력하지 않으면 단순하게 줄바꿈 합니다.
print("# 아무 것도 입력하지 않으면 단순하게 줄바꿈 합니다.")
print("---확인 전용 선---")
print()
print()
print("---확인 전용 선---")


# In[ ]:


#문자열 내부에 따옴표 삽입하기
print("----\"안녕하세요\"----")
# \n은 new line, \t는 tab

print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")


# In[ ]:


#여러 라인에 문자열 만들기
print("동해물과\n백두산이\n마르고 닳도록\n하느님이\n보우하사\n우리나라 만세")


# In[ ]:


#아니면 """ """ 로 묶어서 가능
print("""
동해물과
백두산이
마르고 닳도록
하느님이
보우하사
우리나라 만세
""")


# In[ ]:


#문자열 연산
#덧셈기호 -> 문자열끼리 붙이는 기능
#곱셈기호 -> 문자열을 반복함


# In[ ]:


#문자열 연산자 : +
print("안녕" + "하세요")
#res=안녕하세요
print("안녕하세요" * 3)
#res=안녕하세요안녕하세요안녕하세요


# In[ ]:


#문자열 인덱싱
# 안녕하세요
# 01234
# -5 -4 -3 -2 -1
str_s = "안녕하세요"
print(str_s)
print(str_s[0],str_s[2])
print(str_s[-5])

#문자열 범위 선택 연산자 ":"
print(str_s[1:4])

#문자열 범위 over
##print(str_s[5])
#error msg->IndexError: string index out of range

#문자열 길이 재는 함수
print(len(str_s))


# In[ ]:


#str = "임의로 문자를 넣으세요"
#str 길이를 구해서 처음 문자를 - 방향 인덱스로 구해서 출력하세요
str_s = "show me the money"
str_rev_index = (len(str_s) * -1 )
print(str[str_rev_index])
#또는
print(str_s[-len(str_s)])


# In[ ]:


#숫자 :정수 , 실수
#연산자 : 사칙연산, //(몫), %(나머지), **(거듭제곰)
print("10 + 5=", 10 + 5)
print("10 - 5=", 10 - 5)
print("10 * 5=", 10 * 5)
print("10 / 5=", 10 / 5)
print("10 // 3=", 10 // 3)
print("10 % 3=", 10 % 3)
print("10 ** 5=", 10 ** 5)


# In[1]:


# int() -> 정수로 변환
pi = 3.14159
print(int(pi+2))
print(pi - 2)
print(pi * 2)

print("string " + "10")

str(10)+"strig"


# In[5]:


#복합 대입 연산자
num = 100
num += 10
num += 20
num += 30
print("num=",num)

str_val = "abcd"
str_val += "test"
str_val *= 2
print("str_val=" , str_val)


# In[9]:


#input() -> 키보드로 부터 문자열을 입력 받는 함수, 반듯이 받을 변수 기입해야 한다
str_val = input("문자열 입력>")
print(str_val)

#input("받는 변수 없이 하면 문자열 입력>")

#문자열을 입력 받아 문자열의 길이를 출력하고 처음 글자와 마지막 글자 출력
print("첫번째:",str_val[0], ", 마지막:", str_val[len(str_val) - 1])


# In[11]:


#
num_1 = int(input("숫자 1>"))
num_2 = int(input("숫자 2>"))

str_val = input("문자열 입력>")

print(" a + b = ", num_1 + num_2)
print(" a - b = ", num_1 - num_2)
print(" a * b = ", num_1 * num_2)
print(" a / b = ", num_1 / num_2)

print(str_val * num_1)


# In[ ]:





# In[ ]:




