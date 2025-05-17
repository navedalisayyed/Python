import re
#{2}---Exactly 2 character 
'''
text="This is a pythonnnn and python aaa xyzaaaa"
#path="python{2}"
path=r"\bxyza{4}\b"
print(re.findall(path,text)) 
'''
#{2,4}---2 ,3 and 4 times
'''
text="xaz asdfa sdf xaaz xaaaaaaaz xaaaaz"
path=r'\bxa{1,4}z\b'
print(re.findall(path,text))
'''
#{2,}---2 or more chareacter

'''
text="xaz asdfa sdf xaaz xaaaaaaaz xaaaaz"
patt=r'\bxa{2,}z\b'
print(re.findall(patt,text))
'''

#+ --one or more time

#*--zero or more time

#?--once or none
