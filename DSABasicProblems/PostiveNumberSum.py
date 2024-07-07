#This Program is Only when number is greater than or equal to 0
def check_number(num):
    number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]
    newNum=""
    for digit in num:
        if digit not in number:
            break
    else:
         newNum+=digit
    if len(newNum)==len(num):
        return True
    else:
        return False

def sumOfNumber(arr):
    sum=0
    for i in arr:
        sum+=int(i)
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
        askToAddnumber=input("Do yo want to add one more number yes/no :- ")
        if askToAddnumber.lower()!="yes":
            break
        
print("The Sum of {} Number is {}".format((len(numbers)),sumOfNumber(numbers)))
    





# def twoNumberSum(arr):
#     sm=0
#     for i in range(len(arr)):
#         sm+=arr[i]
#     print("The Sum of {} number is {}".format(len(arr),sm))

# #Taking Input From user 
# #  num=int(input("Enter How Many number of sum do yo want :- "))
# arr=[]
# # for i in range(1,num+1):
# #     number=eval(input("Enter {} Number :- ".format(i)))
# #     if type(number) is int or type(number) is float:
# #         arr.append(number)
# #     else:
# #         print("Entered number is not valid, Please Enter Again")
# #         i-=1
# i=1
# while i>=0:
#     number=eval(input("Enter {} Number :- ".format(i)))
#     if type(number) is int or type(number) is float:
#         arr.append(number)
#         i+=1
#         confiurmation=input("Do you want to enter one more number yes/no:-")
#         if confiurmation.lower()!="yes":
#             break
#     else:
#         print("Entered number is not valid, Please Enter Again")
#         i-=1
# #Calling Function
# twoNumberSum(arr)
