
import csv
'''
req_file="C:\\Users\\SA20508925\\Desktop\\info.csv"

fo=open(req_file,"r")
content=fo.readlines()

data=csv.reader(content)
for each in data:
    print(each)
fo.close()


print(next(content))
#print(f"the heade is {header}")
fo.close()

'''

req_file="C:\\Users\\SA20508925\\Desktop\\demo.csv"

fo=open(req_file,'w')

csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['Sr_NO','Name','Age'])


fo.close()



