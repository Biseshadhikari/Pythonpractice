x = "10"
y = 20
z = True
a = 10.5

print(type(x))
print(type(y))
print(type(z))
print(type(a))


x = "10" 
y = 20 
z = 10.5
print(int(z))
print(float(y))
print(type(x))

print(x+str(y))

print(int(x)+y)


x = 100
y = 7

print(int(x/y))







name = "bisesh adhikari"

if name == "bisesh adhikari":
    print('Welcome '+name)

else:
    print('Welcome Guest')

print("what is your name")
x = input("What is your name? ")

print("Welcome "+x)





x = input("Enter the first number")
y = input("Enter the second number")

sum = int(x)+int(y)
print(sum)



x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

sum = x+y
print(sum)


x = int(input("Enter the first number:")) 
y = int(input("Enter the second number:"))
operator = input("Enter the operator:") 

if operator == "+": 
    print(x+y)
elif operator == "-":
    print(x-y) 
elif operator == "/":  
    print(x/y)
else:
    print("No operator available!!!!")






x = True
while x:
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    operator = input("Enter the operator")

    if operator == "+": 
        print(x+y)
    elif operator == "-":
        print(x-y) 
    elif operator == "/":  
        print(x/y)
    else:
        print("No operator available!!!!")

    askuser = input("Do you want to close this application? y for yes and n for no")
    if askuser == "y":
        x = False







list = ["10.5","20.5"]
newlist = []
for i in list: 
    newlist.append(float(i)*2)

print(newlist)



