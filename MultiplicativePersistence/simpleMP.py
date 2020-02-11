# Bharath
# Try with the number 277777788888899
import os
os.system('cls||clear')
number=int(input("Enter a number :"))
print("The entered number is :",number)
def persistant(n):
    step=0
    while len(str(n))>1:
        final=1
        step+=1
        for i in str(n):
            final*=int(i)
        print("Step no",step,"Value is",final)
        n=final 
    print("Total No of steps is :",step)
persistant(number)