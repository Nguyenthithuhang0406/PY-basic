#Numpy (Numeric Python) là một thư viện cung cấp hỗ trợ cho việc tính toán trên mảng nhiều chiều.

#cài đặt: bằng cmd: pip install numpy

#import thư viện: import numpy as np

#tạo mảng 1 chiều với kiểu dữ liệu mặc định: a = np.array([1,2,3,4,5])
#tạo mảng 1 chiều với kiểu dữ liệu cụ thể: a = np.array([1,2,3,4,5], dtype = int)

#tạo mảng 2 chiều: a = np.array([[1,2,3],[4,5,6]])
#tạo mảng 2 chiều với kiểu dữ liệu cụ thể: a = np.array([[1,2,3],[4,5,6]], dtype = int)

#khởi tạo với các hàm có sẵn
# np.zeros((2,3), dtype = int) tạo mảng 2 chiều với tất cả các phần tử là 0, kích thước 2x3
# np.ones((2,3,4), dtype = int) tạo mảng 3 chiều với tất cả các phần tử là 1, kích thước 2x3x4
# np.full((2,3), 5, dtype = int) tạo mảng 2 chiều với tất cả các phần tử là 5, kích thước 2x3
# np.eye(3, dtype = int) tạo ma trận đơn vị 3x3
# np.arange(1,10,2) tạo mảng 1 chiều với các phần tử từ 1 đến 10, cách nhau 2 đơn vị
# np.random.random((2,3)) tạo mảng 2 chiều với các phần tử ngẫu nhiên từ 0 đến 1, kích thước 2x3

#dtype: kiểu dữ liệu của mảng
#shape: kích thước của mảng
#ndim: số chiều của mảng
#size: số phần tử của mảng

#truy cập phần tử
# arr[i] truy cập phần tử thứ i của mảng 1 chiều
# arr[i,j] truy cập phần tử ở hàng i, cột j của mảng 2 chiều
# arr[n, i, j] truy cập phần tử chiều n, hàng i, cột j của mảng 3 chiều
# arr[a:b] truy cập các phần tử từ a đến b-1 của mảng 1 chiều
# arr[a:b, c:d] truy cập các phần tử từ hàng a đến b-1, cột c đến d-1 của mảng 2 chiều
# arr[:,:i] truy cập tất cả các hàng, cột từ 0 đến i-1 của mảng 2 chiều

#các hàm thống kê
# np.min(arr) tìm giá trị nhỏ nhất
# np.max(arr) tìm giá trị lớn nhất
# np.sum(arr) tính tổng các phần tử
# np.mean(arr) tính trung bình cộng
# np.median(arr) tính trung vị

#toán tử numpy array

#BTVD: 

import numpy as np
#nhập 1 mảng 2 chiều các số thực A (m hàng, n cột) từ bàn phím
#nhập m, n
m = int(input("nhập m: "))
n = int(input())
#khởi tạo mảng A
A = np.zeros((m,n), dtype = float)
#nhập mảng A
for i in range(m):
    for j in range(n):
        A[i,j] = float(input())

#tìm giá trị nhỏ nhất và lớn nhất trên mỗi cột của mảng A
#tìm giá trị nhỏ nhất và lớn nhất theo chiều được chỉ định bởi tham số axis
#axis = 0: theo cột, trả về 1 mảng, giá trị min/max của mỗi cột
#axis = 1: theo hàng, trả về 1 mảng, giá trị min/max của mỗi hàng
#axis = None: trả về 1 giá trị min/max của toàn bộ mảng

# min_col = np.min(A, axis = 0)
# max_col = np.max(A, axis = 0)
# print(min_col)
# print(max_col)

#tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của phần tử này
#tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A
min_A = np.min(A)
max_A = np.max(A)
#in ra giá trị và chỉ số hàng, cột của phần tử lớn nhất
# print(max_A)
# index_max = np.where(A == max_A)
# print(index_max[0][0], index_max[1][0])

#in ra giá trị và chỉ số hàng, cột của phần tử nhỏ nhất
# print(min_A)
# index_min = np.where(A == min_A)
# print(index_min[0][0], index_min[1][0])

#Trong mảng A có bao nhiêu phần tử bằng phần tử lớn nhất của mảng A
index_max = np.where(A == max_A)
print("có : " , len(index_max[0]) ," phần tử bằng phần tử lớn nhất của mảng A")


