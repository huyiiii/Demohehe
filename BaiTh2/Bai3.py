a = int(input("Nhap = "))
s =0
d=0
while(a != 0):
    s += a
    a = int(input("Nhap = "))
    d = d+1
print("Tong cua day so vua nhap la: ",s)
print("TBC Day so vua nhap la: ",s/d)