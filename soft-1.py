for i in range(100):
    if i % 7 == 0:
        print(i)  #7의 배수 출력 (100이하)

print((50 + 45 + 33 + 39 + 29 + 30) / 6) #python 평균 값 구하기

print(round((50 + 45 + 33 + 39 + 29 + 30) / 6, 1)) # python round 함수를 이용해서 첫번째 소수점 까지 출력

number = [1,2,3,4,5,6,7,8,9]
for item in number:
    print(2 * item) # 구구단 2단 표현

for item in range(2,9):
    for each in range(2,9):
        print(item * each) # 구구단 2단 부터 9단까지 표현(답만 출력)
        print(item, "X", each, "=", item * each ) # 문자열 formatting을 이용하지 않은것(문제와 답 동시에 출력)
        print('%d X %d = %d' %(item, each, item * each)) # 문자열 formatting을 이용함(문제와 답 동시에 출력)

        