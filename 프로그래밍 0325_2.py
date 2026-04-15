#5장 리스트
'''
score = [87,84,95,67,88,94,63]
names = ['영호','순자','영식','순희',score]
addressbook=[['영호',25,'010-0000-0000'],['철수',35,'010-0000-0000']]
for i in addressbook:
    print(i)  #i는 숫자열, 문자열 둘 다 받을 수 있음 -> 문자

ri = list(range(5))
print(ri)

myString='apple'

for ch in myString:
    print(ch)
    
listString = list(myString)
print(listString)
'''
#리스트의 항목의 추가와 삭제 (append사용으로 항목 추가)
'''
a_list=['a','b','c','d','e']
a_list.append('f')
print(a_list)
'''

#리무브 메소드로 삭제하는 방법 (리무브로 항목 삭제)
'''
n_list = [11,22,33,44,55,66]
print(n_list)
n_list.remove(44)
print(n_list)


#pop 사용 -> 맨 뒤에 수 없애기
n_list = [11,22,33,44,55,66]
a = n_list.pop()
print(a)
print(n_list)
'''
'''
#멤버 연산자: in, not in
a_list =[10,20,30,40]
print(10 in a_list)

print(50 in a_list)

print(10 not in a_list)


# 리스트에 적용되는 내장함수

#리스트의 메소드
list1=[20,10,40,50,30]
list2 =sorted(list1) #sort를 사용하여 밑에서부터 순서정렬
print(list1)
print(list2)
'''

#리스트의 크기 비교
list1=[1,2,3,4]
list2=[2,3,3,4]
print(list1>list2)
print(list1<list2)

















