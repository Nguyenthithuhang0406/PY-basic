#Bai3
a = int(input("nhap so nguyen duong de kiem tra: "))
ktra = True
i = 2
while (i ** 2 <= a and ktra == True):
    if(a % i == 0):
        ktra = False
    else:
        i += 1
if ktra == True:
    print(a, " la so nguyen to!")
else:
    print(a, " khong phai la so nguyen to!")