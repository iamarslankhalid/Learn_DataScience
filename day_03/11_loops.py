#while and for loops

#while loops
x=0
while (x<=5):
    print(x)
    x=x+1

#for loops
for x in range (5,10):
    print(x)

# array
days = ["Mon" , "Tues" , "Wed" , "Thurs" , "Fri" , "Sat" , "Sun"]

for d in days:
    if (d=="Fri"):break #loops stop
    if (d=="Friday"):continue #skip to next iteration
    print(d)