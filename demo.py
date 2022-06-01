n = int(input("N = "))
m = int(input("M = "))
a = [200,500,1000,2000,5000]
s= 0
d=0
for i in range(0,5):
    if(s < m and d < m):
        s += a[i]
        d = d+1
        print(s)