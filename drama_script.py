import os,re

# 드라마 대본 실습


f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()

print(script101[:100])

print ([x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))])