<<<<<<< HEAD
'''
#6-1 딕셔너리의 생성

capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print(capital_dic['Korea'])

fruits_dic = {'apple':'5000','banana':'4000','grape':'5300','melon':'6500'}
print("apple의 가격은", fruits_dic['apple'], "원입니다.")


#6.2 딕셔너리의 항목 추가와 삭제
person={'이름':'홍길동','나이':26,'몸무게':82,'특기':'분신술'}
person['특기']='분신술'
person['아버지'] ='홍판서'
del person['나이']
print(person)


#6-3 딕셔너리와 연산
capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)


#6.4 딕셔너리의 활용
fruits_dic = {'apple':'6000','melon':'3000','banana':'5000','orange':'7000'}
print(fruits_dic.keys())
print(fruits_dic.values())
print(fruits_dic.pop('apple'))
print(fruits_dic)
print(fruits_dic.clear())


#6.5 딕셔너리의 활용
fruits_dic = {'apple':'6000','melon':'3000','banana':'5000','orange':'4000'}
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print('fruits_dic 딕셔너리의 항목의 개수:',len(fruits_dic))
if 'apple' in fruits_dic:
    print('apple is in fruits_dic.')

if 'mango' not in fruits_dic:
    print('mango is not in fruits_dic.')


#6.6 튜플의 생성과 패킹, 언패킹
the_day = (1919,3,1)
year, month, day = the_day
print(f'{year}년 {month}월 {day}일은 삼일절입니다.')


list = [10,20,30]
a,b,c = tuple(list)
a,b,c =c,b,a
print(f'a={a},b={b},c={c}')


#6-7 튜플의 활용
person = ('홍길동',2019001,179)
f_list = list(person)
f_list[1] = 202003
person = tuple(f_list)
print('학번 변경 후 person=',person)

#6-8 튜플의 반환
def square(x,y):
    return x**2,y**2
x=10
y=20
x_sq,y_sq = square(x,y)
print('{}제곱 = {}, {}제곱={}'.format(x,x_sq,y,y_sq))

result = (10,20,30) +(40,50,60)
print(result)

print('Hello'*3)
print(('Hello',)*3)


#6-9 집합의 생성
lst = ['apple','mango','banana']
s1 ={'apple','mango','banana'}
print(s1)

greet = 'Good afternoon'
s2 ={'r','t','n','','G','o','e','f','a','d'}
print(s2)


#6-10 집합의 연산
s1 ={10,20,30,40}
s2 ={30,40,50,60,70}
print(s1&s2)
print(s1-s2)
print(s1^s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))


#6-11 곱집합의 연산
def product_set(X, Y):
    result = set()
    for x in X:
        for y in Y:
            result.add((x, y))
    return result

A = {1, 2}
B = {'A', 'B', 'C'}

print('A =', A)
print('B =', B)

print('A*B =', product_set(A, B))
print('B*A =', product_set(B, A))
print('A*A =', product_set(A, A))
print('B*B =', product_set(B, B))
'''

#6-12 복수로 주사위를 던졌을 때 특정값 이상을 얻을 확률 구하기
def tuple_sum(tup):
    if isinstance(tup,int):
        return tup
    else:
        accum = 0
        for element in tup:
            accum += tuple_sum(element)
    return accum

def product_set(set1,set2):
    res =set()
    for i in set1:
        for j in set2:
            res = res|{(i,j)}
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res

dice ={1,2,3,4,5,6}
outcomes = exp(dice,3)
print(f"주사위를 세 번 던져 발생할 수 있는 사건은 {len(outcomes)}가지 경우가 존재합니다.")

count = 0
for case in outcomes:
    if tuple_sum(case) >= 10:
        count += 1
print(f"주사위를 세번 던져 눈의 합이 10 이상인 경우의 수는 {count}가지입니다.")

outcomes = exp(dice,3)
total = len(outcomes)
def prob_over(x):
    count=0
    for case in outcomes:
        if tuple_sum(case) >= x:
            count += 1
    prob = count/total *100
    return prob
for x in range(3,19):
     print(f"눈의 합으로 {x}이상 얻을 확률 {prob_over(x):.2f}%")

=======
'''
#6-1 딕셔너리의 생성

capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print(capital_dic['Korea'])

fruits_dic = {'apple':'5000','banana':'4000','grape':'5300','melon':'6500'}
print("apple의 가격은", fruits_dic['apple'], "원입니다.")


#6.2 딕셔너리의 항목 추가와 삭제
person={'이름':'홍길동','나이':26,'몸무게':82,'특기':'분신술'}
person['특기']='분신술'
person['아버지'] ='홍판서'
del person['나이']
print(person)


#6-3 딕셔너리와 연산
capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)


#6.4 딕셔너리의 활용
fruits_dic = {'apple':'6000','melon':'3000','banana':'5000','orange':'7000'}
print(fruits_dic.keys())
print(fruits_dic.values())
print(fruits_dic.pop('apple'))
print(fruits_dic)
print(fruits_dic.clear())


#6.5 딕셔너리의 활용
fruits_dic = {'apple':'6000','melon':'3000','banana':'5000','orange':'4000'}
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print('fruits_dic 딕셔너리의 항목의 개수:',len(fruits_dic))
if 'apple' in fruits_dic:
    print('apple is in fruits_dic.')

if 'mango' not in fruits_dic:
    print('mango is not in fruits_dic.')


#6.6 튜플의 생성과 패킹, 언패킹
the_day = (1919,3,1)
year, month, day = the_day
print(f'{year}년 {month}월 {day}일은 삼일절입니다.')


list = [10,20,30]
a,b,c = tuple(list)
a,b,c =c,b,a
print(f'a={a},b={b},c={c}')


#6-7 튜플의 활용
person = ('홍길동',2019001,179)
f_list = list(person)
f_list[1] = 202003
person = tuple(f_list)
print('학번 변경 후 person=',person)

#6-8 튜플의 반환
def square(x,y):
    return x**2,y**2
x=10
y=20
x_sq,y_sq = square(x,y)
print('{}제곱 = {}, {}제곱={}'.format(x,x_sq,y,y_sq))

result = (10,20,30) +(40,50,60)
print(result)

print('Hello'*3)
print(('Hello',)*3)


#6-9 집합의 생성
lst = ['apple','mango','banana']
s1 ={'apple','mango','banana'}
print(s1)

greet = 'Good afternoon'
s2 ={'r','t','n','','G','o','e','f','a','d'}
print(s2)


#6-10 집합의 연산
s1 ={10,20,30,40}
s2 ={30,40,50,60,70}
print(s1&s2)
print(s1-s2)
print(s1^s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))


#6-11 곱집합의 연산
def product_set(X, Y):
    result = set()
    for x in X:
        for y in Y:
            result.add((x, y))
    return result

A = {1, 2}
B = {'A', 'B', 'C'}

print('A =', A)
print('B =', B)

print('A*B =', product_set(A, B))
print('B*A =', product_set(B, A))
print('A*A =', product_set(A, A))
print('B*B =', product_set(B, B))
'''

#6-12 복수로 주사위를 던졌을 때 특정값 이상을 얻을 확률 구하기
def tuple_sum(tup):
    if isinstance(tup,int):
        return tup
    else:
        accum = 0
        for element in tup:
            accum += tuple_sum(element)
    return accum

def product_set(set1,set2):
    res =set()
    for i in set1:
        for j in set2:
            res = res|{(i,j)}
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res

dice ={1,2,3,4,5,6}
outcomes = exp(dice,3)
print(f"주사위를 세 번 던져 발생할 수 있는 사건은 {len(outcomes)}가지 경우가 존재합니다.")

count = 0
for case in outcomes:
    if tuple_sum(case) >= 10:
        count += 1
print(f"주사위를 세번 던져 눈의 합이 10 이상인 경우의 수는 {count}가지입니다.")

outcomes = exp(dice,3)
total = len(outcomes)
def prob_over(x):
    count=0
    for case in outcomes:
        if tuple_sum(case) >= x:
            count += 1
    prob = count/total *100
    return prob
for x in range(3,19):
     print(f"눈의 합으로 {x}이상 얻을 확률 {prob_over(x):.2f}%")

>>>>>>> 44b42a59c536fbf3d1fb78a7851405150d035a22
