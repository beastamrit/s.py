def abc(n,number):
    mass=1
    if (n & mass)==1 or (n&mass)==0:
        if (number &(1<<(n-1))):
            print("set")
        else:
            print("not set")
number=int(input("enter a number"))
n=int(input("enter a number"))
abc (n,number)