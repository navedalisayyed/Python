x=56
print(type(x))
y=str(x)
print(type(y))
z=bool(x)
print(type(z))
p=0
print(p,type(p))
q=bool(p)
print(q,type(q))

#Type conversion in python

#Note:-Any data type can be converted to boolean
#bool(any_data_type)=True or False
# bool(empty)=False--->bool(0),bool(None),bool([]),bool(()),bool({})
#bool(non-empty)=True--->Remaining will come as True

#x=""   is also False

#Any data type can be converted into string but reverse is not always true
'''
x=5.6
print(int(x))
my_name="python"
print(int(my_name))
'''
arr=[]
new=""
digits = [9]
for digit in digits:
   new+=str(digit)
new=int(new)
new=new+1
new=str(new)
print(new)
print(len(new))
for i in range(len(new)):
   arr+=[int(new[i])]
print(arr)   