#Bai 2
n = int(input("nhap so nguyen n: "))
luy_thua = 1
#vi range se tu 0 den n-1
for i in range(n + 1):
    if i != 0:
        luy_thua = luy_thua * i
print("n! = ", luy_thua)
