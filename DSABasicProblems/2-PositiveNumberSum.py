#This Program is Only when number is greater than or equal to 0
def check_number(num):
    number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]
    newNum=""
    for digit in num:
        if digit not in number:
            break
        else:
            newNum+=digit
    print(newNum)
    if len(newNum)==len(num):
        return True
    else:
        return False

def sumOfNumber(arr):
    sum=0
    for i in arr:
        sum+=eval(i)
    return sum
numbers=[]

while True:
    userNumber=input("Enter the number to find the sum:- ")
    if check_number(userNumber)==True:
        numbers.append((userNumber))
        # print(type(numbers[0]))
        askToAddnumber=input("Do yo want to add one more number yes/no :- ")
        if askToAddnumber.lower()!="yes":
            break
    else:
        print("Invalid Input, Please enter a number.")
        askToAddnumber=input("Do you want to add one more number yes/no")
        if askToAddnumber.lower()!="yes":
            break
        
print("The Sum of {} Number is {}".format((len(numbers)),sumOfNumber(numbers)))
    
