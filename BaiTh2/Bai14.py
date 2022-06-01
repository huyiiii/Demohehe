s1 = s2 =0
n = int(input("Nhap N = "))
x = int(input("Nhap X = "))
for i in range(1,n+1):
    s1 += x**i/i
print("Tong S1 = ",s1)

def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
 
for i in range(1,n+1):
    s2 += x**i/giaiThua(i)
print("Tong S2 = ",s2)