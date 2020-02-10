import os
os.system('cls||clear')

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BharathMaths"]
mycol = mydb["MultiplicativePersistence"]

start=int(input("Enter the Starting Value:"))
end=int(input("Enter the Ending Value :"))
#threshold=int(input("Enter the least step Size value :"))

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
    bhadict={"Number":data,"Steps":step}
    mycol.insert_one(bhadict)
    print (data,"steps ->",step) 

i=start
while (i<=end):
    persistant(i)
    i+=1
