
import Function_imp
def mul(a,b):
    print(f"The mul of {a} and {b} is {a*b}")
    return None

def main():
   x=10
   y=20
   Function_imp.addition(x,y)
   #mul(x,y)
   return None

if __name__== "__main__":
    main()
'''    
import Function_imp
print("This is from script2",__name__)
'''

print(__name__)