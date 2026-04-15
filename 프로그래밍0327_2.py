'''
#연속적인 값의 생성과 누적 덧셈
s=0
for i in range(1,11):
    s=s+i
print('1에서 10까지의 합:',s)


#누적 덧셈의 중간 결과 출력하기
s = 0
for i in range(1, 11):
    s = s + i
    print('i = {}, s = {}'.format(i, s) )
print('1에서 10까지의 합:', s)

'''
# 사용자로부터 입력을 받은 후 누적 합계 값 구하기
n = int(input('합계를 구할 수를 입력하세요 : '))
s = 0
for i in range(0, n) :
    s = s + (i+1)
print('1부터 {}까지의 합은 {}'.format(n, s))
