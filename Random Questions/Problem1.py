# Maximum Tree Height 

# Solving wihtout usign any in-built function to build logics
# Shorting the array
def shortedArr(arr):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    removeDuplicates(arr)

# removing duplicates from arrays

def removeDuplicates(arr):
    newArr=[]
    for i in range(0,len(arr)):
        if i <len(arr)-2:
            if arr[i]!=arr[i+1] :
                newArr.append(arr[i])
        else:
            if arr[i-1]!=arr[i]:
                newArr.append(arr[i])
            

    # print(newArr)
    treeWater(newArr)   

# Maximum Height of the tree 
def treeWater(arr):
    Height=0;
    for i in range(0,len(arr)):
        Height+=arr[i]
    print("Maximum Height of the tree is :- ",Height)

# Taking Input From user
#  first input for length of the array
#  second input for array elements
userInput=int(input("Enter the Number of Element in the List :- "))

# using inbuilt eval function
# userInput2=eval(input("Enter the Element in the List :- "))

# without taking eval() function
arr=input("Enter the Number of Element in the List :- ")
userInput2=[]
if arr!="":
    num=""
    for i in range(0,len(arr)):
        if i==len(arr)-1:
            num+=arr[i]
            userInput2.append(int(num))
        if arr[i]!=" ":
            num+=arr[i]
        else:
            userInput2.append(int(num))
            num=""
    
        
                
# print(userInput,len(userInput2),userInput2,len(arr))
# checking Number of element and length of arr is equal or not
if userInput==len(userInput2):
    if userInput>1:
        shortedArr(userInput2)
    else:
         print("Maximum Height of the tree is :- ",userInput2[0])
else:
    print("length Mismatch ")