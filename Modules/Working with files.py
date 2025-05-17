'''
fo=open('newdemo.txt','w')
#print(fo.mode)
#print(fo.readable())
print(fo.writable())

fo.close()
'''
'''
my_content=["This is a first data\n","This is a second data"]
fo=open("random.txt",'w')
#fo.write("This is a first line\n")
#fo.write("This is a second line")
fo.writelines(my_content)
fo.close()
'''
'''
my_cotent=["This is using loop-1","This is using loop-2","This is using loop-3"]

fo=open("with loop.txt","w")

for each_line in my_cotent:
    fo.write(each_line+"\n")
fo.close()    
'''
'''
fo=open("with loop.txt","r")
#print(fo.read())
data=fo.read()

fo.close()
print(data)
'''
'''
fo=open("with loop.txt","r")
data=fo.readlines()
fo.close()
for each in range(3):
    print(data[each])
'''

#copy file into another file using python

sfile="with loop.txt"
dfile="newrandaom.txt"

sfo=open(sfile,"r")
content=sfo.read() #read is string,readline is string,readlines is list
sfo.close()

dfo=open(dfile,"w")
dfo.write(content)
dfo.close()