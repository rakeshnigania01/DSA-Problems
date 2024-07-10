#WAP to print the Numbers in Vertical lines but numbers are in Decending Order

"""
O/P
5
4
3
2
1
"""

print("Print Numbers in vertival line with numbers are in decendig order :- ")

# Using while loop
def pattern6M1(N):
    print("Method 1 Output :- ");
    i=N;
    while(i>0):
        print(i);
        i-=1;

#  using for loop
def pattern6M2(N):
    print("Method 2 Output :- ")
    for i in range(N,0,-1):
        print(i)

# Taking Input from User
userInput=int(input("Enter a Number :- "));

# Calling the functions
pattern6M1(userInput);
pattern6M2(userInput);