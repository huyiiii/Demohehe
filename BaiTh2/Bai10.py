n = int(input("Nhap N = "))
s=0
d=0
def check(a):
    count = 0
    if(n==1):
        return False
    else:
        for i in range(2,a):
            if(a%i == 0):
                count += 1
    if(count == 0 ):
        return True
    else:
        return False
for i in range(2,n+1):
    if(check(i) == True):
        s += i
        d += 1
print("Tong cac so nguyen to la: ",s)
print("TBC cac so nguyen to la: ",s/d)