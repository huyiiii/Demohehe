import math
n = int(input("Nhap N = "))
d =0
s =0
def check(a):
    b = int(math.sqrt(a))
    if b**2 == a:
        return True
    else:
        return False
for i in range(1,n+1):
    if(check(i) == True):
        print(" ",i)
        s += i
        d += 1
print("Tong cua cac so chinh phuong la: ",s)
print("TBC cac so chinh phuong la: ",s/d)
        
