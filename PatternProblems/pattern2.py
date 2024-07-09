#write a program to print the number in horizontal line
#Ouptut :- 1 2 3 4 5 6 7 8 9 10

#Method 1
def numberprintM1(N):
    beg=""
    i=1
    while i<=N:
        beg+=str(i)+" "
        i+=1
    print(beg)
numberprintM1(int(input("Enter a Number and number > 0 :- ")))