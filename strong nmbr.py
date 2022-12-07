#  STRONG NUMBER

num=int(input("enter the number"))
s=0
strong=num
while strong>0:
        f=1
        i=1
        r=strong%10
        while i<=r:
                f=f*i
                i=i+1
        s=s+f
        strong=strong//10
if s==num:
        print("strong number")
else:
        print("not")