n = int(input("N = "))
s = 0
d=0
print("Uoc so cua N theo thu tu tang dan: ")
for i in range(1,n+1):
    if (n%i == 0):
        s = s+i
        print(" ",i)
        d += 1
print("TBC cac uoc so cua ",n," la ",s/d)