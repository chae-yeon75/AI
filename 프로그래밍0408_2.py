<<<<<<< HEAD
'''
#6-6 튜플의 생성과 패킹, 언패킹

tuple = (1,2,3)
tuple[0] = 1
print(tuple[0])
#>>item을 지정할 수 없다고 뜸 -> 튜플은 변경할수없는형태이기때문에 튜플0번째 수를 바꾸려해도 바꿔지지 않음

def plusmius(a1,a2):
    return a1+a2,a1-a2
output = plusmius(10,2)
print(type(output))
#>> <class'tuple'>이라고 뜸-> 튜플은 변경 불가능 <교환불가능속성>


def plusmius(a1,a2):
    return a1+a2,a1-a2
output = plusmius(10,2)

output_list = list(output) #아웃풋을 리스트 변수로 변경
print(type(output_list))
'''
#패킹: 하나의 변수에 여러 개의 값을 넣는 것을 의미
#언패킹: 패킹된 변수가 있으면 여기에서 여러 개의 값을 꺼내오는 것
#스왑: a,b = b,a라는 한 줄을 이용하여 값을 교환 -> 코드나 효율성 면에서 간단하고 직관적임




















=======
'''
#6-6 튜플의 생성과 패킹, 언패킹

tuple = (1,2,3)
tuple[0] = 1
print(tuple[0])
#>>item을 지정할 수 없다고 뜸 -> 튜플은 변경할수없는형태이기때문에 튜플0번째 수를 바꾸려해도 바꿔지지 않음

def plusmius(a1,a2):
    return a1+a2,a1-a2
output = plusmius(10,2)
print(type(output))
#>> <class'tuple'>이라고 뜸-> 튜플은 변경 불가능 <교환불가능속성>
'''

def plusmius(a1,a2):
    return a1+a2,a1-a2
output = plusmius(10,2)

output_list = list(output)
print(type(output_list))
>>>>>>> 44b42a59c536fbf3d1fb78a7851405150d035a22
