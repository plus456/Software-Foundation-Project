# def 함수 알아보기
def add(a,b):
    return print(a + b)

add(50, 4)

# def 함수를 이용해서 계산기 만들기
def calculation(a, b):
    symbols = input("연산자를 입력하세요: ")
    if(symbols != "+" and symbols != "-" and symbols != "x" and symbols != "/"):  #올바른 연산자를 입력하였는지 확인하는 함수
        return print("올바르지 않은 입력입니다.")
    if(symbols == "x"):         # 연산자 입력 값에 따른 출력 값이 달라짐
        return print(a * b)
    if(symbols == "/"):
        return print(a / b)
    if(symbols == "+"):
        return print(a + b)
    if(symbols == '-'):
        return print(a - b)

calculation(50, 4)


#if-else 문 복습
def seperate():
    a = int(input("자연수 중 하나를 입력하세요: "))
    if(a < 0):
        return print("올바르지 않은 입력입니다.")
    if(a % 2 == 0):
        print("짝수")
    else:
        print("홀수")

seperate()
"""
부가가치세 계산하기
소비자 가격 = 물건 가격 * 1.1
물견 가격 = 소비자 가격 * 10/11
부가세 = 물건 가격 * 0.1 = 소비자 가격 * 1/11
"""

5000 * 1.1 # 부가세 포함 가격 출력


5500 / 1.1 # 부가세 제외 물건의 원 가격 출력

8000 / 1.1 # 8000원 점심을 먹었을 때 원래 물건 가격을 계산

round(8000 / 1.1, 1) # round 함수를 사용해서 소수점 첫째 자리까지 계산

# 부가세 출력 프로그램
# 서비스 종류가 총 a,b,c 가 존재하고, 부가세가 존재하는지 안하는지 선택가능
# a = 23만원 b = 40만원 c = 67만원 

def service_price():
    service = input("서비스 종류를 입력하세요, a/b/c: ")    #input 값을 통해 서비스 종류 확인
    valueAdded = input("부가세를 포함합니까? y/n: ")        #input 값을 통해 부가세 포함 여부 확인
    if(service != "a" and service != "b" and service != "c"):  #service 종류를 정확하게 입력하였는지 확인하는 함수
        return print("올바르지 않는 입력입니다.")       
    if(valueAdded != "y" and valueAdded != "n"):            #valueAdded의 값을 정확하게 입력하였는지 확인하는 함수
        return print("올바르지 않은 입력입니다.")
    if valueAdded == "y":               #valueAdded 값이 y일 경우 service 종류에 따른 result 값 생성
        if service == "a":
            result = 23 * 1.1
        if service == "b":
            result = 40 * 1.1
        if service == "c":
            result = 67 * 1.1
    if valueAdded == "n":               #valueAdded 값이 n일 경우 service 종류에 따른 result 값 생성
        if service == "a":
            result = 23
        if service == "b":
            result = 40
        if service == "c":
            result = 67
    print(round(result,1), "만 원입니다.")      #result 값을 첫 번째 소수점 자리까지 반올림하여 출력

service_price()