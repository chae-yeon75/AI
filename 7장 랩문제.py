'''
#7.1
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day =now.day
hour=now.hour
minute = now.minute
second = now.second
if hour < 12:
    period = "오전"
    display_hour = hour
else:
    period = "오후"
    display_hour = hour - 12
    if display_hour == 0:  # 12시 처리
        display_hour = 12

print(f">> 오늘의 날짜:{year}년{month}월{day}일, 현재시간: {period} {display_hour}시 {minute}분 {second}초")

#7.2
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year,today.month,today.day))
xMas = dt.datetime(2026,12,25)
time_gap = xMas -dt.datetime.now()
print('2026년 크리스마스까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds//3600))

import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year,today.month,today.day))
Newyear = dt.datetime(2027,1,1)
time_gap = Newyear -dt.datetime.now()
print('2027년 새해까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds//3600))

import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year,today.month,today.day))
xMas = dt.datetime(2026,7,5)
time_gap = xMas -dt.datetime.now()
print('2026년 생일까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds//3600))


#7.3 날짜 계산하기
from datetime import datetime, timedelta
today = datetime.today()
after_1000 = today + timedelta(days=1000)


#7.4
import math
for i in range(2,11):
    print(f"4**{i} = {math.pow(4,i)}")
    
    
import math
for degree in range(0,181,10):
    radian = math.radians(degree)
    print(f"{degree}degree = {radian:.3f}radian")
    
import math
for degree in range(0,181,10):
    radian = math.radians(degree)
    value = math.sin(radian)
    print(f"sin({degree})={value:.2f}")
 '''

#7.5
import random
multiples_of_5 = [i for i in range(0,101) if i%5==0]
result = random.sample(multiples_of_5,3)
print('0에서 100이하의 정수 중에서 5의 배수')
print(result)

import random
result = random.sample(range(1, 11), 3)
print("1에서 10 사이의 임의의 정수 :", result)










