'''
1.Conditional: if-else , if -elif
2.Loop: for loop, while loop
3.Jumping : break, continue, pass
'''

def checkAge(age):
    if(age>18):
        print('Age is greater than 18')
    else:
       print('Age is less than 18')
checkAge(20)
# wap to display 'child if age is below 18, dispaly 'Adult' if age is greater than 18.
# dispaly senoir citizen if age is above 65.

def displayAge(age):
    if(age<18):
        print('Child')
    elif(age>18 and age<65):
        print('Adult')
    elif(age>65):
            print('Senior Citizen')
    dispalyAgeCateg(int(input('Enter the age:')))