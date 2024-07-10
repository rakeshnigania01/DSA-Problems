# WAP to print number in vertical lines
"""
O/P
1
2
3
"""
print("Print Numbers in Vertical Lines :-")
# Method 1
# Using While Loops
def pattern5M1(N):
    print("Method 1 O/P :- ")
    i=1;
    while(i<=N):
        print(i);
        i+=1;

# Using For Loop
def pattern5M2(N):
    print("Method 2 O/P :- ")
    for i in range(1,N+1):
        print(i)

# Taking Input
userInput=int(input("Enter a Number :- "))

# Calling Functions
pattern5M1(userInput)
pattern5M2(userInput)