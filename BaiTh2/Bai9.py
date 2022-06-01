import math
n = int(input("Nhap N = "))

for i in range(n,3*n +1):
    a = int(math.sqrt(i))
    if (a**2 == i):
        print("SCP ",i)