# without input and without return statement
def add():  # here the declare thefunction of python
    a = 10
    b = 20
    print('Addition:', a + b)

add()

#with input and without return statement

def sub(a, b):
    print('Subtraction:', a - b)
  
sub(20, 10)
#without input and with return statement:


def mul():
    return 10 * 20

#with input and with return  statement:
def div(a, b):
    return a / b
print(mul())
print(div(20, 10))  