'''
#3-6 반복문 이용
for i in range(5):
    print('Hello,Python!')
    
for i in range(0,5):
    print(i)

#3-7 range()함수
a_list = list(range(2,101,2))
print(a_list)
b_list = list(range(1,101,2))
print(b_list)
c_list = list(range(-99,0))
print(c_list)


#3-8 누적 덧셈의 응용
sum = 0
for i in range(1,101):
    sum += i
print(sum)

sum_a = 0
for i in range(0,101,2):
    sum_a += i
print(sum_a)

sum_b = 0
for i in range(1,101,2):
    sum_b += i
print(sum_b)
'''

#3-9 패턴 출력 응용
for i in range(7):
    for j in range(6-i):
        print(' ',end=' ')
    print('#')









