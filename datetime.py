import datetime
x = datetime.datetime.now()
print(x.month)

import datetime
x = datetime.datetime.now()
print(x)

#to create new file and add my name also close the file 
f = open("laxmi.txt", "w")
f.write("My name is laxmi sharma, is mca student")
f.close()

f = open("laxmi.txt", "r")
print(f.read())

#while print 1 to 10
i = 1
while i < 11:
    print(i)
    i=i+1

