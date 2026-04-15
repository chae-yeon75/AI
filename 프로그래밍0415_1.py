'''
#7.4 수학 관련 모듈 (math모듈)
#ceil(올림값), floor(내림값)
import math as m
print(m.sin(90.0))
print(m.sin(m.pi/2.0))

#7.5 랜덤모듈
import random as rd  #random()함수: 0이상 1미만의 임의의 실수를 반환함
a = rd.random()
print(a)

import random as rd  
a = list(range(1,11))  #1에서 10까지의 연속적인 정수 생성
rd.shuffle(a)
print(a)


#7.6.1 터틀 초기화와 모양 바꾸기
import turtle as t   #별도의 윈도우가 화면에 나타나고 커서가 그림을 그림
t.setup(width=400, height=400)
for i in range(200):
    t.forward(i)
    t.left(93)
t.done()


#7.8 Tkinter 모듈
#중간고사에 Tk모듈 안들어감 -> 7장 앞부분만 시험

#8장 예외 처리와 파일
#8.1 오류와 예외처리의 필요성
#8.2 try-except문의 문법
try:
    a=1/0
except:
    print('0으로 나누지 마세요!') #->프로그램이 사용자에게 대처할수있는 방법 제시

# 루프를 사용하여 정확한 숫자가 입력될 때까지 루프 돌리기
while(True):
    try:
#        a,b = input('두 수를 입력하시오:').split() #split은 빈칸으로 수 구분하는 것
#        result =int(a)/int(b)
        a,b = map(int,input('두 수를 입력하시오:').split(',')) #위의 두 문장을 한문장으로 줄여주는 map 
        print('{}/{}={}'.format(a,b,result))
        break
    except:
        print('수가 정확한지 확인하세요.')

str3 = input('세 개의 숫자를 입력하세요:').split()
istr3=map(int(str3))
print(str3)
    
a,b,c=map(int,input('세 개의 숫자를 입력하세요:').split())
print(a,b,c) #위의 3줄을 2줄로 줄일수있는 map
'''
#get_ans함수는 우리가 할 수 있는 게 아니야. 일단 넘어가자
#8장은 시험에 거의 안들어가는듯 한게 없어 교수님왈: 가볍게 보세요~

#9장 클래스와 객체 지향 프로그래밍
#함수가 뭔지 아세요? def plus(a,b): return a+b 의 형식이 함수임
#클래스변수는 information을 가짐 -> 정보를 가지고 수행하는 함수
# 예) animals.sort() :animal은 리스트로 항목을 원소로 가지고 있고 sort()라는 함수를 가지고 있음

#9.3 클래스와 객체,인스턴스
# 클래스: 프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체

class Cat: #cat이라는 클래스 생성: 생성자(초기화 메소드)
    def __init__(self,name,color='흰색'): #만들어진 고양이가 self가 됨, 함수에는 셀프가 들어가야함
        self.name = name
        self.color = color
        #셀프에 속한 name, color이라는 인스턴스 변수 생성 -> 고양이의 정보를 출력하는 메소드
    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹야옹~~'.format(self.name,self.color))
        
nabi = Cat('나비','검정색') #나비, 네로, 미미라는 인스턴스 생성
nero = Cat('네로','흰색')
mimi = Cat('미미','갈색')

nabi.meow()
nero.meow()
mimi.meow()

#9.5까지 시험 범위인가봐...
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






