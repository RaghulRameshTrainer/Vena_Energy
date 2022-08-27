import re

'''
match
search
findall
sub
split
compile-finditer
'''
#match
line="pet:cat i love cat pet:dog i love dog"
#result=re.match(r'pet:cat',line,re.I)
# result=re.match(r'\w+:\w+',line,re.I)
# print(result.group(0))

#search
# result=re.search(r'pet:d..',line,re.I)
# print(result)

# result=re.findall(r'\w+:\w+',line,re.I)
# print(result)

#print(re.sub('love','like', line))
#print(re.split(' ',line))

mystr="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

~!@#$%^&*()_+}{|":?><

https://www.amazon.com
http://www.amazon.com
https://amazon.com
https://www.amazon.co.in

123-244-2461
345_542_5454
424 665 4754
432.676.5436

raghulramesh@gmail.com
raghul_ramesh@yahoo.com
ramesh@outlook.com
raghul.ramesh@gmail.com

Ha HaHa
+91-9887211199
9887211199
98872111999
988111111
8887211199
7887211199
6887211199
5887211199
4887211199
3887211199
2887211199
1887211199
"""
pattern=re.compile(r'\+?9?1?\-?\b[6789]\d{9}\b')
#pattern=re.compile(r'~!@#\$%\^&\*\(\)_\+}{\|":\?><')
#pattern=re.compile(r'\W+')
#pattern=re.compile(r'\bHa\b')
#pattern=re.compile(r'(\w+\.)?\w+@\w+\.com')
#pattern=re.compile(r'\d{3}[\-_\s]\d{3}[\-_\s]\d{4}')
#pattern=re.compile(r'https?://(www\.)?\w+\.com?(\.in)?')
#pattern=re.compile(r'.')
matches=pattern.finditer(mystr)
for x in matches:
    print(x.group(0))