import os
import re

def refinder(pattern, script):    
    if re.match(pattern, script):     #Match 메서드는 문자열의 처음 부분만 비교 검색
        print('Match!')
    else:
        print('Not a match!')

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script)


pattern = r'is'
script = 'Life is so cool'
print(re.search(pattern, script).group())    #search 메서드는 문자열 전체에서 패턴을 찾음 match와 비슷하지만 search는 모든 구간에서 비교

number = 'My number is 981223-1****** and yours is 991021-2******'
print(re.findall('\d{6}', number)) # \d{6}은 숫자를 6번 반복한 패턴 이라는 뜻
# findall 메서드는 문자열 내에서 패턴을 모두 찾아 리스트 형태로 반환 search와 match와는 다르게 찾지 못하면 빈 리스트로 반환

sentence = 'I have a lovely dog, really. I am not telling a lie'
print(re.findall(r'\w+ly', sentence)) # sentence에서 ly로 끝나는 단어를 추출

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
print(re.findall(r'\d.+?년',example1))  # 년이라는 글자를 찾으면 패턴 멈춤

print(re.findall(r'\d+.년', example1))  # 숫자를 반복하다가 '년'이라는 글자로 끝나는 패턴

#마침표(.)은 모든 문자를 의미하는 정규표현식으로 모든 문자를 반환합니다.
#이 때 ?를 사용하면 원하는 문자에서 패턴을 멈춤

example = '이동민 교수는 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 학자는 이 문제에 대해 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'
print(re.findall(r'\(.+\)', example))  #첫 괄호와 마지막 괄호 사이에 모든 문자를 출력함
print(re.findall(r'\(.+?\)',example))  # 괄호와 괄호 사이의 문자만 출력함

sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', sentence))  #., ?, !을 기준으로 나눔

print(re.sub(r'dog', 'cat', sentence)) # 모든 dog를 cat으로 바꿔서 출력

words = 'I am home now. \n\n\nI am with my cat.\n\n' #이렇게 하면 공백이 발생
print(re.sub(r'\n', '', words)) # 이렇게 공백 제거도 가능함.
