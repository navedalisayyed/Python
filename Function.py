#1.Introduction to function
#2.Defining Function
#3.Calling Function
#4.Default Parameters
# 5.Variable-Length Parametrs
# 6.Return Statement

#Default Parameters:
'''
def greet(name1="Guest"):
    print(f"Hello {name1} Welcome")

greet("krish")   

###Varibale length arguement
##Positionl and keyword Arguement

def print_numbers(*args,**kwargs ): #*args are positional argument which denotes normal values
    for value in args:              #**kwargs are keyword aregument which denotes key value pairs
        print(f"postional argument is {value}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_numbers(1,2,3,4,"Sayyed",name="sayyed",age=32,country="India")

#Lambda Function

#Syntax
#lambda arguement:expression
'''

##VRT function details

###Function with argument

def get_result(num): #paramater or positional arguments
    result=num+10
    print(f"your result is : {result}")
    return None
def main():
    #global num
    num=eval(input("enter the number: "))
    get_result(num)   #Argument 
    return None
main()

###Function with argument with return value

##Function with defaul argument

def display(a=1):
    print("This is value of a: ",a)
    return None
display(4)
display(5)
display()

def add_numbers(a,b=0):  #u can define default positional argument at the end not at beginning i.e (a=0,b)
    result=a+b
    print("The result is ",result)
    return None
add_numbers(4,5)
add_numbers(5)
add_numbers(7)

##Function with varibale length argument












