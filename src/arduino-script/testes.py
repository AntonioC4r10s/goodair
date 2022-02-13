import re

text = 'umidade: 84.0, pessoas: 12'
ntext = re.split(': |, ', text)
print(ntext[1])
print(ntext[3])