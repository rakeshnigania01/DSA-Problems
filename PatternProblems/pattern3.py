# Print  The number in Horizontal line But number should be in decending order
# O/P = 5 4 3 2 1

# Using while loop sand storing in beg variable

print("This Function will print the number like 5 4 3 2 1")
def pattern3M1(N):
    print(" Method 1 output ")
    beg=""
    i=N
    while i>0:
        beg+=str(i)+" "
        i-=1
    print(beg)

#  Using  for loop and python in-built function () means wihtout using beg variable 
def pattern3M2(N):
    print(" Method 2 Ouptut ")
    for i in range(N,0,-1):
        print(i, end=" ")
    print()

userNumber=int(input("Enter a Number "))
pattern3M1(userNumber)
pattern3M2(userNumber)