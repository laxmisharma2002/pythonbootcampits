#tuple can store the multiple values
myTuple = ("Ivan","Anshu","Wani","Manisha","Wani")
print(myTuple)
print(type (myTuple))
      

print(myTuple[1])

#it shows us error
# myTuple(1) = "Laxmi"
# print(myTuple)

for name in myTuple:
    print(name)

#dictionary can store multiple data in key value pair 
myDict = {
    "name":"Laxmi Sharma",
    "email":"shivanisharma73967@gmail.com",
    "mob":"7011588512"
}

print(type(myDict))

print(myDict)

for item in myDict:
    print(myDict[item])

myDict["nama"] = "Manisha"
print(myDict)

#oops
#class and object
# class Sonal:
#     print("Im from ghaziabad")
# x = Sonal()

# #create object an pass class proporties
# Sonal = Sonal()
# print(Sonal.age)


#calculate age
class agecalculator:
    bornyear = int(input("enter the born year"))
    currentyear = int(input("enter the current year"))
    age=currentyear-bornyear
a = agecalculator()
print(a.age)
