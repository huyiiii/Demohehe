def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
 
s = 0
n = int(input("Nhap N = "))
for i in range(1,n+1):
    s += 1/giaiThua(i)
print("Tong S = ",s)