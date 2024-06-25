n=int(input("enter a number:"))
digit=int(input("enter a digit:"))
rev=0
count=0
temp=n
while n>0:
    rem=n%10
    if rem==digit:
        count=count+1
    rev=rev*10+rem
    n=n//10
print(count)
