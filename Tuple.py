lst=list() #type is list
print(type(lst))
tpl=tuple()# type is tuple
print(type(tpl))

#Note:-Tuple can be converted to list and vice versa

numbers=tuple([1,3,4,6])
print(numbers)

num=list((1,3,4,6))
print(num)

#Multiple date type in tuple

tpl=(1,"Hello World",4.3,True)
print(tpl)

#Accessing/Slicing the Elements in tuple(Silimar like list)

##Tuples operation

concatenateion_tuple= numbers + tpl
print(concatenateion_tuple)

print(tpl * 3)  ## multiplication will multilply every element by 3
print(numbers * 3)


##Immutable nature of Tuple

##Tuple methods

print(numbers.count(1))
print(numbers.index(3))

##packing and unpacking Tuple
#packing
packed_tuple=1,"Hello",3.4
print(packed_tuple)

#unpacking

a,b,c=packed_tuple
print(f"{a} {b} {c}")

##unpacking with *

numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)

##Nested Tuple
#List
lst=[[1,2,3],[4,5,6,],[1,"Hello",2.4,True]]
print(lst[0][1])

print(lst[2][2:])

##tuple

Nested_tuple=((1,2,3),(4,5,6),(1,"Hello",2.4,True))

print(Nested_tuple[2][1])

for sub_tuple in Nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")
    print()    