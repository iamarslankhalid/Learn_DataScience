x = 10
y = 10.2
z = "Hello"

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z))  # <class 'str'>

# when mulitply any integer wwith float its class chnage to float from integer

#iplicit type conversion
x = x*y
print(type(x)) # <class 'float'>
x = x+y
print(x, "Type of x is: " , type(x))

#explicit type conversion
age=input("What is your age? ")
age=int(age)
print(age, type(int(age)))
print(age, type(float(age)))
print(type(age))

name=input("Enter your name ")
print(name, type(name))