'''
#5-1 리스트의 생성
even_list=[2,4,6,8,10]
print(even_list)

even_list = list(range(2,11,2))
print(even_list)

nations = ['Korea','China','India','Nepal']
print(nations)


friends = ['길동','철수','은지','지은','영민']
print(friends)

string =['X','Y','Z']
print(string)


#5-2 리스트의 생성과 인덱싱
prime_list=[2,3,5,7]
print('prime_list의 첫 원소:',prime_list[0])
print('prime_list의 마지막 원소:',prime_list[3])
print('prime_list의 마지막 원소:',prime_list[-1])

nations = ['Korea','China','Russia','Malaysia']
print('nations의 첫 원소:',nations[0])
print('nations의 마지막 원소:',nations[-1])
print('nations의 마지막 원소:',nations[len(nations)-1])


#5-3 리스트의 삽입과 삭제, in연산자
prime_list=[2,3,5,7]
prime_list.append(11)
print(prime_list)
prime_list.remove(3)
print(prime_list)

nations = ['Korea','China','Russia','Malaysia']
nations.append('Nepal')
print(nations)

if 'Japan'in nations:
    print('Japan는(은) 국가 목록에 있습니다.')
else:
    print('Japan는(은) 국가 목록에 없습니다.')
    
if 'Russia'in nations:
    print('Russia는(은) 국가 목록에 있습니다.')
else:
    print('Russia는(은) 국가 목록에 없습니다.')


#5-4 리스트의 min(),max(),sum(),len()함수
prime_list=[2,3,5,7]
print(min(prime_list))
print(max(prime_list))
print(sum(prime_list))
print(len(prime_list))

nations=['Korea','China','Russia','Malaysia']
print(min(nations))
print(max(nations))

#5-5 리스트 메소드의 응용
a =[1,2,3]
b=[10,20,30]
a.append(b)
print(a)

a=[1,2,3]
b=[10,20,30]
a.extend(b)
print(a)

nlist=[1,2,3,4,5,6,7,8,9,10]
nlist.insert(0,0)
print(nlist)


nlist=[0,1,2,3,4,5,6,7,8,9,10]
nlist.reverse()
print(nlist)
nlist.pop()
print(nlist)


#5-6 리스트 연산
list1=[1,2,3]
list2 = list1 * 3
print(list2)
    
list3= list1 * 4
print(list3)
'''
#5-7 리스트의 슬라이싱
n_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
n_list=list(range(15))
print('n_list=',n_list)
s_list1 = n_list[0:5]
s_list2 = n_list[5:11]
s_list3 = n_list[11:15]
s_list4 = n_list[2:11:2]
s_list5 = n_list[10:5:-1]
s_list6 = n_list[10:1:-2]

print("s_list1 =", s_list1)
print("s_list2 =", s_list2)
print("s_list3 =", s_list3)
print("s_list4 =", s_list4)
print("s_list5 =", s_list5)
print("s_list6 =", s_list6)












