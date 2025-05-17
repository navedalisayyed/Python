'''
#my_list=[]
list1=["apple","banana","cherry","kiwi","guava"]

#bool(empty_list)= False
#bool(no_empty_list)= True

#modifiying the list

list1[1]="watermelon"
print(list1)

#List method

list1.append("orange") 
print(list1)   

list1.insert(1,"banana")
print(list1)

#list1.remove("banana") #Remove first ocurrence of an item
#print(list1)

list1.pop() # Remove and return last element
print(list1)    

list1.insert(2,"banana")
print(list1)
print(list1.count("banana"))

##Slicing

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

#Iterating over list

for index,number in enumerate(numbers): #enumerate will return indexes
    print(index,number)

#List comprehension

##Basic List comprehension
#[expression for item in iterable]

square=[num**2 for num in range(10)]
print(square)

##List Comprehension with condition
##with conditional logic [expression for item in iterable if condition]

lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
print(lst)      

even_num=[num for num in range(10) if num%2==0]
print(even_num)

##Nested list comprehension

##[expression for item1 in iterable1 for item2 in iterable2]

lst1=[1,2,3,4]
lst2=["a","b","c","d"]

pair=[(i,j) for i in lst1 for j in lst2]
print(pair)

##List comprension with function calls

words=["hello","world","python","list","comprehension"]
lengths=[len(word) for word in words]
print(lengths)
'''
#prac=["apple","banana","cherry","kiwi","guava"]

#print(range(prac[4:-1:-1]))

nums = [1, 1, 0, 1, 1, 1]

count=0

for num in range(len(nums)):
    if nums[num] == 1:
        count+=1
    else:
        count=0
print(count)    
          