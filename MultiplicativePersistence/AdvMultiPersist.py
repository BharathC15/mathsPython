# Bharath
# Try with the number 277777788888899
import os
os.system('cls||clear')

start=int(input("Enter the Starting Value:"))
end=int(input("Enter the Ending Value :"))
threshold=int(input("Enter the least step Size value :"))

def persistant(data):
    n=data
    step=0
    while len(str(n))>1:
        final=1
        step+=1
        m=[int(x) for x in str(n)]
        for i in m:
            final*=i
        n=final 
    if(step>=threshold):
        print (data,"steps ->",step)

i=start
while (i<=end):
    persistant(i)
    i+=1