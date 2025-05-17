'''
My_str="Python"
print(My_str.startswith('P'))
print(My_str.endswith('hon'))
print(My_str.islower())
print(My_str.istitle())
print(My_str.isalnum())
print(My_str.isalpha())
'''
str="python"
print("-".join(str))

str1="Python"
str2="Python scripting"
str3="string operation"

print(str1.center(20))

print(f"{str1.center(20)}\n{str2.center(20)}\n{str3.center(20)}")

#zfill(padding)

#Strip and Split

x=" python "
print(x.strip()) #Any charactor at beginning and ending will remove by Strip operation
y="python scripting is easy"

print(y.strip('easy'))

z="python scripting is python"

print(z.rstrip('python')) #Will remove 'python' at right side

print(z.lstrip('python')) #Will remove 'python' at left side

x='pythonyy'

print(x.strip('p').strip('yy'))

# count,index and find

x="python is easy and popular langauge"

print(x.count('p'))

print(x.index('p',1))

print(x.find('p',20))

print(x.find('python'))