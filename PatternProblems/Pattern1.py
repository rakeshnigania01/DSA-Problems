#Print Star in Single line (Horizontal line)
def starPrinting1(N):
    print("Method 1")
    i=0
    while i<N:
        print("*",end=" ")
        i+=1
    print()
    print("================================================\n\n\n")


def starPritingM2(N):
    print("Method 2")
    i=0
    beg=""
    while i<N:
        beg+="*"+" "
        i+=1
    print(beg)
    print("================================================\n\n\n")

userInput=int(input("Enter a Number :- "))
starPrinting1(userInput)
starPritingM2(userInput)