'''string=input("enter a word:")
if string==string[::-1]:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome.")'''

'''lst=[]
n=int(input("enter number of elements: "))
for i in range(0,n):
    element=int(input("enter the elements:"))
    lst.append(element)
print(lst)'''


#double and square
'''n=int(input())
for i in range(n+1):
    if(i%2==0):
     print(2*i)
    else:
     print(i**2)'''

#star hash pattern
'''n=int(input())
for i in range(0,n):
    print()
    for j in range(n,i,-1):
        if(j%5==0):
            print("#",end="")
        else:
            print("*",end="")'''

#euclidean distance
'''import math
x1=float(input("enter x1 coordinate:"))
x2=float(input("enter x2 coordinate:"))
y1=float(input("enter y1 coordinate:"))
y2=float(input("enter y2 coordinate:"))
print("x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2)

x=(x2-x1)**2
y=(y2-y1)**2

g=x+y
h=math.sqrt(g)
print(round(h,2))'''


'''a=input("enter a word:")
for i in a:
    print(i,end=' ')'''

#decimal to binaqry
def decimalTobinary(n):
    if(n>1):
        decimalTobinary(n//2)
    print(n%2,end=' ')

a=int(input("enter number:"))
print(decimalTobinary(a))



