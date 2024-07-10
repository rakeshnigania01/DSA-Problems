#  Write a program to print the star in a vartical line
"""
O/P 
*
*
*
*
"""
print("WAP to print the star in vertical line")
# using while loop
def pattern4M1(N):
    print("Method 1 ouput ")
    i=1;
    while(i<=N):
        print("*");
        i+=1;


#  using for loop

def pattern4M2(N):
    print("Method 2 output ")
    for star in range(1,N+1):
        print("*") 

# Taking Input
userNumber=int(input("Enter a number to print * :-"))
pattern4M1(userNumber);
pattern4M2(userNumber);