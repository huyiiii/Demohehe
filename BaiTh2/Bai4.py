import math
n = int(input("Nhap N = "))
while(n<0):
    n = int(input("Nhap N = "))
for i in range(1,n+1):
    a = int(math.sqrt(i))
    if (a*a == i):
        print("SCP ",i)
    