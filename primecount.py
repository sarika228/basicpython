n=int(input("enter a number:"))
pc=0
i=1
while pc<n:
    j=1
    c=0
    while j<=i:
        if j%i==0:
            c=c+1
        j=j+1
    if pc==2:
        pc=pc+1
        print(i,"prime number")
        # pc=pc+1
    # if pc==n:
    #     break
    i=i+1