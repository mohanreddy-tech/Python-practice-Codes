
'''

1.conditional: if-else, if elif
2.looping: for, while
3.control: break, continue, pass
4.function: def, return
'''

def checkAge(age):
    if(age>18):
        print("You are eligible to vote")
    elif(age==18):
        print("You are not eligible to vote")
    checkAge(18)
    # Wap to dispaly 'child' if age is in below 18, display 'adult' is age is above 18,
    # display senior citizen if age is above 65.

    def displayAgeCateg(age):
        if(age<18):
            print("Child")
        elif(age>=18 and age<=65):
            print("Adult")
        elif(age>65):
            print("Senior Citizen")
            displayAgeCateg(int(input("Enter your age: ")))