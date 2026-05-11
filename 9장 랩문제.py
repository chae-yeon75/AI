#9-1부터 9-10까지

#9-1
print((200).__sub__(100))
print((200).__mul__(100))
print((200).__truediv__(100))

print([10,20,30,40].pop())

#9-2
#객체지향 프로그래밍: 잘 설계된 클래스를 이용하여 객체 생성
#절차적 프로그래밍: 데이터들이 많아지면 많은 함수 호출 필요 (대규모 어려움)
#그래픽 사용자 인터페이스

#9-3
#클래스: 프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체
#객체: 어떤 행위의 대상이 될 수 있는 모든 사물
#인스턴스: 클래스로부터 만들어지는 각각의 개별적인 객체
#클래스의 속성
#클래스의 동작

#9-4
class Dog:
    def bark(self):
        print('멍멍')
my_dog = Dog()
my_dog.bark()

#9-5
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print('멍멍~~')
my_dog = Dog('Jindo')
my_dog.bark()

#9-6
class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Dog(name={self.name})"
my_dog = Dog('Jindo')
print('my_dog의 정보:',my_dog)

#9-7
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is not m')

#9-8
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y=y
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)


v1 = Vector(30, 40)
v2 = Vector(10, 20)

# 곱셈과 나눗셈 출력
print("v1 * v2 =", v1 * v2)
print("v1 / v2 =", v1 / v2)

# 음의 벡터 출력
v3 = Vector(10, 20)
print("-v3 =", -v3)
