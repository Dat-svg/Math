import numpy as np
import random as rd
import math

A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
B=np.array([[1,2,3,4],[5,6,7,8]])
C=np.array([[1,2],[3,4],[5,6],[7,8]])

#Hàm dùng để kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return -1
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return -1
        else:
            return 1

def task1a():
    #Transpose: (ma trận chuyển vị của ma trận A B C)
    a = np.transpose(A)
    b = np.transpose(B)
    c = np.transpose(C)
    #tạo ma trận temp để tính tổng ma trận A ban đầu và ma trận chuyển vị của A
    temp = np.add(A, a)
    #tạo ma trận temp1 để tính tổng của tích ma trận C và ma trận B 
    #với tích ma trận chuyển vị B và ma trận chuyển vị C
    temp1 = np.add(C @ B, b @ c)
    result = np.add(temp,temp1)
    return result

def task1b():
    #Khởi tạo ma trận 10x10 với toàn số 0
    result = 0
    for i in range(1,11):
        #dùng hàm tính toán lũy thừa của ma trận
        result += pow((A/(i+9)),i)
    return result

def task1c():
    #Trích xuất các hàng ở vị trí lẻ trong ma trận A
    A_odd = A[::2]
    return A_odd

def task1d():
    #Kết quả trả về là một mảng một chiều chứa tất cả phần tử lẻ của ma trận A
    A_odd_int = A[A % 2 == 1]
    return A_odd_int

def task1e():
    #Khởi tạo mảng rỗng để lưu trữ các số nguyên tố
    A_prime = []
    #Duyệt qua các phần tử trong ma trận và tạo một vector gồm các số nguyên tố
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if (is_prime(A[i][j]) == 1):
                A_prime.append(A[i][j])
    return np.array(A_prime)

def task1f():
    #Nhân hai ma trận B và C
    D = C.dot(B)
    #Duyệt các hàng chẵn
    for i in range(0, np.shape(D)[0], 2):
        #Đối với i khi duyệt qua, thực hiện phép biến đổi trên dòng đó
        #Có nghĩa là lấy tất cả các phần tử của hàng i theo thứ tự đảo ngược.
        #Gán giá trị của hàng đó bằng kết quả của phép ngược đó
        D[i,:] = D[i, :: -1]
    return D

def task1g():
    #khai báo biến đếm
    count = 0
    temp = [0]*np.shape(A)[0]

    for i in range(0, np.shape(A)[0]):
        for j in range(0, np.shape(A)[0]):
            #kiểm tra số nguyên tố
            if (is_prime(A[i][j])==1):
                #nếu là số nguyên tố thì tăng biến đếm
                count = count + 1
        # Thêm số đã đếm vào mảng chứa biến đếm
        temp[i] = count
        # Kết thức vòng lặp cho biến đếm trở về 0
        count = 0
    
    for i in range(len(temp)):
        #tìm cột có số lượng số nguyên tố nhiều nhất
        if temp[i] == max(temp):
            print(A[i])

def task1h():
    #Mảng để thực hiện lưu kết quả
    odd_length = []
    for row in A:
        #khai báo biến đếm
        count = 0
        max_len = 0
        for num in row:
            if num % 2 == 1:
                #Nếu là phẩn tử lẻ thì tăng biến lên 1 
                count += 1
                #Giá trị lớn nhất được lưu trong biết max_len
                max_len = max(max_len, count)
            else:
                #Nếu không phải là phần tử lẻ thì biến trở lại 0
                count = 0
        #lưu giá trị lớn nhất vào odd_length
        odd_length.append(max_len)
    max_odd_length = np.max(odd_length)
    #trả về tất cả các hàng trong ma trận A có giá trị của odd_length bằng với giá trị lớn nhất
    result = np.where(odd_length == max_odd_length)[0]
    return A[result]

#main
print(A)
print("---------------------------------")
print("a) Result: \n", task1a())
print("b) Result: \n", task1b())
print("c) Odd rows of the matrix A into a new matrix is: \n", task1c())
print("d) Odd interger numbers in the matrix A into a new vector is: \n", task1d())
print("e) Prime numbers in the matrix A into a new vector: \n", task1e())
print("f) Reverse elements in the odd rows of the matrix D is: \n", task1f())
print("g) Regarding the matrix A, the rows which have maximum count of prime numbers is:")
task1g()
print("h) Regarding the matrix A, the rows which have the longest contiguous odd numbers sequence is: \n", task1h())
