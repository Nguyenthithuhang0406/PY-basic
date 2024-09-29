print("hello world!!!")
#ghi chu

#chuoi co dang la 1 comment
print("#day la comment")

#số nguyên
a = 4
print(type(a)) #lấy ra kiểu dữ liệu

#số thực
b = 1.96
print(type(b))


#lấy toàn bộ nội dung của thư viện decimal (import decimal)
from decimal import *

#lấy tối đa 30 chữ số pần nguyên và phần thập phân
getcontext().prec = 30

print(Decimal(10)/Decimal(3))

#phân số
from fractions import *

frac = Fraction(6,9)

print(frac)

print(type(frac))

frac1 = Fraction(1,3)
frac2 = Fraction(1,2)

frac3 = frac1 + frac2

print(frac3)

#số phức
# <phần thực> + <phần ảo>j

c = complex(1,2)
print(c)

#lấy ra phần thực
print(c.real)

#lấy ra phần ảo
print(c.imag)

#biểu thức toán học trong kiểu dữ liệu số

#cộng
print(1+2)

#trừ
print(1-2)

#nhân
print(1*2)

#chia ra số thực
print(10/3)

#chia lấy phần nguyên
print(10//3)

#chia lấy phần dư
print(10%3)

#lũy thừa
print(10**3)

#lấy căn bậc 2
print(10**0.5)

#lấy căn bậc 3
print(10**(1/3))

from math import *
#lấy giá trị tuyệt đối
print(abs(-10))

#làm tròn
print(round(1.5))

#làm tròn xuống
print(floor(1.5))

#làm tròn lên
print(ceil(1.5))

#lấy giá trị lớn nhất
print(max(1,2,3,4))

#lấy giá trị nhỏ nhất
print(min(1,2,3,4))

#ép kiểu
print(int(1.5))

#ước chung lon nhất
print(gcd(10,15))

# vân vân lên doc xem

