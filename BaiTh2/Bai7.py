n = int(input("Nhap N = "))
def check(n):
    count = 0
    if(n==1):
        print(n," khong la so nguyen to")
    else:
        for i in range(2,n):
            if(n%i == 0):
                count += 1
    if(count == 0 ):
        print(n," la so nguyen to")
    else:
        print(n," khong la so nguyen to")
check(n)