def is_fibonacci(n):
    a=0
    b=1
    while b<n:
        temp=b
        b=a+b
        a=temp
    return b==n or n==0
n=int(input("enter a number:"))
if is_fibonacci(n):
    print(n,"belongs to the fibonacci sequence.")
else:
    print(n,"does not belong to the fibonacci sequence.")
