import re
text="it is python learn andlearn it is easy to learn"


#^---Matches string at the start of line
'''
patt="^i[ts]"
print(re.findall(patt,text))
'''
#$---Matches at the end of line

'''
patt="learn$"
print(re.findall(patt,text))
'''
#/b--Empty string at the begining or end of the word
'''
#patt=r"\blearn"
patt=r"\blearn\b"
print(re.findall(patt,text))
'''

#\B--Empty string not at the begining or end of word

patt=r"\Blearn\B"
print(re.findall(patt,text))

#\t,\n,\r--Matches tab,newline,and return repectively


