import os,re

f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()

print(script101[:100])

print ([x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))])