#python script for digits in a number and sum and reverse of number and palindrome or not.
n=int(input("enter a number:"))
temp=n
s=0
rev=0
while(n!=0):
    rem=n%10
    print(rem)
    s=s+rem
    rev=(rev*10)+rem
    n=n//10
print(s)    
if(rev==temp):
    print("palindrome")

    
    
    
