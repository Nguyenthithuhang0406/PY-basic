#Bai4
n = int(input("nhap so hang cho tam giac vuong: "))

#dung vong lap for de in tam giac
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print() #in xuong dong de sang hang moi
    