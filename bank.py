
f= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
for a in f:
    f=open("bank.txt","a")
    f.write(a)
    f.write("\n")
    f.close()
    