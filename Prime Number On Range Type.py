import math
lis=[]
n=int(input("enter to check if the number is prime or not"))
for i in range(1,10000):
    if((i**2)<n):
        lis.append(i**2)
    if((i**2)>n):
        lis.append(i**2)
        break
another2=lis[len(lis)-1]
another2=int(math.sqrt(another2))
print(another2)
check=[]
for i in range(another2):
    if(i==1):
        continue
    if(i%2!=0):
        print(i)
        if(n%i==0):
            check.append(0)
        else:
            check.append(1)
count=0            
for i in range(len(check)):
    if(check[i]==1):
        count+=1
if(count==len(check)):
    print("prime number for sure")
else:
    print("not a prime number")
