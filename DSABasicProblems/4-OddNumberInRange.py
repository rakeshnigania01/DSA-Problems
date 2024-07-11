#Write a program to find only ODD numbers in a given range 
print("Write a Program to find the odd number from A to B or B to A where A and B are Positive Numbers")

# defining from where to start or where to end
def checkNumbers(num1, num2):
    if num1>num2: 
        # return largerNumber, Smaller numbers for B - A
        checkOddNumbersDecending(num1,num2)
    elif(num1<num2):
        # retrun smallerNumber, largerNumber for A -B
        checkOddNumbersAssending(num1,num2)
    else:
        #Both numbers are same but here we are cheking that number is Odd number or not
        if(num1 %2==1):
            print("Odd numbers {} --- {} is {}".format(num1,num2,num1))
        else:
            print("No Odd numbers in {} --- {} ".format(num1,num2,num1))

# Checking number is odd or not 
def checkOddNumbersAssending(start,end):
    while(start<=end):
        if(start%2==1):
            print("{} is Odd Number ".format(start))
            start+=2
        else:
            start+=1
def checkOddNumbersDecending(start,end):
    while(start>=end):
        if(start%2==1):
            print("{} is Odd Number ".format(start))
            start-=2
        else:
            start-=1

# Taking Input From the User 
#eval() function will take input both int and float values
#int() function will convert float to in 
num1=int(eval(input("Enter first Number :- ")))
num2=int(eval(input("Enter second Number :- ")))

#calling both functions
checkNumbers(num1,num2)
