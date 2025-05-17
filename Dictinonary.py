'''
empty_dic={}
print(type(empty_dic))
empty_dic=dict()
print(type(empty_dic))

student={"name":"krrish","age":"32","grade":24}
print(student)

##Accessing dictinoary element
print(student['grade'])
print(student['age'])

##using get() method
print(student.get('grade'))
print(student.get('age'))
print(student.get('last_name',"Not available")) ##When key is not present in dic then return "Not available instead of None"

##Modifiying the element

student['age']=33 ##update the value for the key 'age'
print(student)
student['address']='india' ## Added new key and value pair
print(student)

##Deleting the key

del student['grade']  ##Key value pair has been deleted
print(student)

##Dictionary Methods

keys=student.keys()
print(keys)
print(type(keys))
values=student.values()
print(values)

print(type(values))

item=student.items() ##will give all key value pair
print(item)

##shallow copy

student_copy=student.copy() ##shallow copy which allow to store student_copy variable as seperate 
                             ##so when i change in student dict will not reflect in student_copy
print(student_copy)
print(student)
student['age']=35

print(student_copy)
print(student)

##Iterating over Dictionaries

for keys in student.keys():
    print(keys)
for value in student.values():
    print(value)
for key,value in student.items():
    print(f"keys are {key} and values are {value}")       
'''
    ##Nested Dictionaries
student_Data={
        "student1":{"name":"krrish","age":30},
         "student2":{"name":"peter","age":35}
 } 
#print(student_Data)
#print(student_Data["student2"]["name"])
#print(student_Data["student2"]["age"])

##iterating over nested dictionary

for student_id,student_info in student_Data.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

##Dictionary comprehension
'''
square={x:x**2 for x in range(5)}
print(square)

##conditional Dictionary comprehension

even={x:x**2 for x in range(5) if x%2==0 }
print(even)


numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1 

print(frequency)   

##Merge 2 dictionaries into one
'''
'''
def maxPairDiff(arr):
    listDiff=[]
    for p,i in enumerate(arr):
        evalList=[e for e in arr[p+1:] if e>i]
        if len(evalList)>0:
            listDiff.append(max(evalList)-i)
    return (max(listDiff))

givenList = [7, 9, 5, 6, 3, 2]
print ("Required result is {}".format(maxPairDiff(givenList)))
'''

