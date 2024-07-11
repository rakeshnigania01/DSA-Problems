#Write a program to find only Even or Multiple of numbers in a given range 
print(" Write a Program to find the Even or Multiple of any number from A to B or B to A where A and B are Positive Numbers \n\n")


#  checking starting ending points and based on the condition call that function
def validateRange(num,start,end):
    if start<end:

        valueAcending(num,start,end)
    elif start > end:
        valueDecending(num,start,end)
    else:
        # my both starting and ending numbers are same but we have to check starting or ending number  is divisble by that Number or not  
        if start % num==0:
            print("{} is multiple of {}".format(start,num))
        else:
            print("Invalid Range ")

# function to find the even/Multiple number in acending order 
def valueAcending(num,start,end):
    i=start;
    while i<=end:
        if i % num==0:
            print("{} is multipe of {} ".format(i,num))
            i+=num
        else:
            i+=1

# Functon to find the Even/Multiple number in Decending Order
def valueDecending(num,start,end):
    i=start;
    while i>=end:
        if i%num==0:
            print("{} is multipe of {} ".format(i,num))
            i+=num
        else:
            i+=1
# taking Input From the user
userInput1=int(input("Do you want to Even numbers Enter 2 or multiple of any Number Enetr that Number :-  "))
# userInput1=int(input("enter the number that you want multiple :-"))
userInput2=int(eval(input("Enter the Number from where to start finding :-")))
userInput3=int(eval(input("Where to end your searching :-")))

# Calling the function
validateRange(userInput1,userInput2,userInput3)