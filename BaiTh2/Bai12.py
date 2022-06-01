s = 0
n = int(input("Nhap N = "))
for i in range(1,n+1):
    s += 1/(i*(i+1))
print("Tong S = ",s)