n = int(input("Nhập N ="))
 
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
 
print (giaiThua(n))
print("A.")
for i in range(1,n+1):
    print("Gia tri ", i,"! = ",giaiThua(i))
print("B.")
for i in range(1,n+1):
    if(i%2 != 0):
        print("Gia tri ", i,"! = ",giaiThua(i))
print("C.")
for i in range(1,n+1):
    if(i%2 == 0):
        print("Gia tri ", i,"! = ",giaiThua(i))