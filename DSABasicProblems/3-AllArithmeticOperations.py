#Addition Function fro 2 numbers and their data type
def addition(num1,num2):
    print("Addition of {} and {} is {}".format(num1,num2,num1+num2))
    print("Type of {} is {}".format("num1",type(num1)))
    print("Type of {} is {}".format("num2",type(num2)))
    print("Type of {} is {}".format("num1+num2",type(num1+num2)))

#Subtraction Function fro 2 numbers and their data type
def subtract(num1,num2):
    print("Subtraction of {} and {} is {}".format(num1,num2,num1-num2))
    print("Type of {} is {}".format("num1",type(num1)))
    print("Type of {} is {}".format("num2",type(num2)))
    print("Type of {} is {}".format("num1-num2",type(num1-num2)))

#Division Function fro 2 numbers and their data type
def divide(num1,num2):
    print("Division of {} and {} is {}".format(num1,num2,num1/num2))
    print("Type of {} is {}".format("num1",type(num1)))
    print("Type of {} is {}".format("num2",type(num2)))
    print("Type of {} is {}".format("num1 / num2",type(num1 //num2)))

#MULTIPLICATION function fro 2 numbers and their data type
def multiply(num1,num2):
    print("Multiply of {} and {} is {}".format(num1,num2,num1*num2))
    print("Type of {} is {}".format("num1",type(num1)))
    print("Type of {} is {}".format("num2",type(num2)))
    print("Type of {} is {}".format("num1 * num2",type(num1*num2)))

#REminders Function fro 2 numbers and their data type
def reminder(num1,num2):
    print("remainder of {} is {}".format(num1,num1%2))
    print("remainder of {} is {}".format(num2,num2%2))


# Taking 2 Numbers as Input from user 
num1=eval(input("Enter first Number :- "))
num2=eval(input("Enter the second :- "))

#Taking Sybolic input from user  for calling function
userImput=input("What u do you want to + , - , / ,* , or  reminder(%) use these syboles :- ")
arr=["+",'-',"*","/","%"]
if userImput in arr:
    if userImput=="+":
        addition(num1,num2)
    elif userImput =="-":
        subtract(num1,num2)
    elif userImput =="*":
        multiply(num1,num2)
    elif userImput == "/":
        divide(num1,num2)
    elif userImput =="%":
            reminder(num1,num2)
else:
    print("Please Enter Right Symbol ")