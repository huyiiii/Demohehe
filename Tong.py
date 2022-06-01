def fibo():
    n = -1
    while(n < 0):
        n = int(input("Nhap n = "))
    A = [0 for i in range(n)]
    A[0]= 0 
    A[1] = 1
    for i in range(2,n):
        A[i] = A[i-1] + A[i-2]
    return n,A
def Xuat(A,n):
    print("In day %d so Fibonacci:" %n, end = "")
    for i in range(n):
        print(" ",A[i],end = "")
        
n,A = fibo()
Xuat(A,n)