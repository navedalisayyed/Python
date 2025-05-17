#serach,match,finditer,findall,split,sub etc
#re.search(pattern,text)
#re.match(pattern,text)
#re.finditer(pattern,text)
#re.findall(pattern,text)
import re

'''
text='This is python and it is easy to learn'
patt='i[ts]'
print(re.findall(patt,text))
'''
#Basic Rules to create pattern

#[abc]--Matches a or b or c 
#[a-c]--Matches a or b or c
#[a-zA-Z0-9]--Matches with letter(a to z) or (A to Z) or (0-9)
#\w--Matches any single letter,digit or underscore

text='This is python2 and it @ is easy -to 3 _learn @.'
'''
patt="\w"
print(re.findall(patt,text))
'''
'''
patt="\w\w"   #Any 2 character combination
print(re.findall(patt,text))
'''
'''
patt="\w\w\w" #Any 3 character combination
print(re.findall(patt,text))
'''
#\W---Matches any character not part of \w

'''
patt="\W"
print(re.findall(patt,text))
'''

#\d---matches Decimal no 0-9
'''
patt="\d"
print(re.findall(patt,text))
'''

#.--Matches any single character(Which are available on keyborad) except newline charecter
'''
patt="."    #Any single charecter
#patt=".."  #Any 2 character
#patt="..." #Any 3 chacarter
print(re.findall(patt,text))
'''
'''
patt="\."  #Match dot with dot
print(re.findall(patt,text))
'''


