#8.1
'''
a = [10,20,30]
a[3] #IndexError

n=int('20%') #ValueError

a=100+'200' #TypeError


try:
    a = [10,20,30]
    a[3]
except Exception as e:
    print(e)

try:
    n = int('20%')
except Exception as e:
    print(e)
    
try:
    a = 100 + '200'
except Exception as e:
    print(e)
'''
#8.2
try:
    result = 10*(30/0)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
    
import sys

f = open('myfile.txt')
s = f.readline()

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


























