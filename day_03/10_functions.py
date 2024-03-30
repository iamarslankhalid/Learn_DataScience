#defining a functions
def print_codanics():
    print("We are learning with codanics")
    print("We are learning with codanics")
    print("We are learning with codanics")

print_codanics()

#2
def print_codanics():
    text = "We are learning with codanics"
    print(text)
    print(text)
    print(text)

print_codanics()

#3 
def print_codanics(text):
    print(text)
    print(text)
    print(text)

print_codanics("We are learning with codanics")

#defining a function with if , elif and else statments
def school_calculator(age , text):
    if age==5:
        print("Join the school")
    elif age>5:
        print ("Higher school")
    else:
        print("Still a baby")

school_calculator(5, "Hammad")

#defing a function of future

def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

future_predicted_age=future_age(18)
print(future_predicted_age)

