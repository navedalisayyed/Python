s = "The quick brown fox jumps over the lazy dog"
count=0
long=0

for word in s:
   if (word != " "):
       count+=1
   elif(count >= long):
       long = count
       count=0
   else:
      count=0

print(long)       
       