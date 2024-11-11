#bai6
import random
so_ngau_nhien = random.randint(1,100)
ktra = False
while ktra == False:
    a = int(input("Nhap so ban du doan: "))
    if a == so_ngau_nhien:
        print("Ban doan dung roi!")
        ktra = True
        break
    if a > so_ngau_nhien:
        print("so nay lon hon so can doan!")
    if a < so_ngau_nhien:
        print("so nay nho hon so can doan!")

