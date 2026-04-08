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