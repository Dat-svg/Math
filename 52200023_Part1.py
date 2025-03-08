import statistics

#Hàm mean():
list_of_numbers = [1,2,3,4,5]
mean = statistics.mean(list_of_numbers)
print('Mean is: ')
print(mean) #Output = 3

#Hàm mean() với giá trị ngoại lai:
list_of_numbers = [1, 2, 3, 4, 5, 1000]
mean = statistics.mean(list_of_numbers)
print('Mean: ')
print(mean) #Output: 169,1666666666666

#Hàm fmean() khi không có trọng số:
list_of_numbers = [1.2, 2.5, 3.4]
fmean = statistics.fmean(list_of_numbers)
print("FMean: ")
print(fmean)

#Hàm fmean() khi có trọng số:
list_of_numbers = [1.2, 2.5, 3.4]
weights = [0.2, 0.3, 0.22]
fmean = statistics.fmean(list_of_numbers, weights)
print("FMean: ")
print(fmean)

#Hàm geometric_mean():
list_of_numbers = [1, 2, 3]
geometric_mean = statistics.geometric_mean(list_of_numbers)
print("Geometric_mean: ")
print(geometric_mean)

#Hàm harmonic_mean():
list_of_numbers = [2, 4, 8]
weight = [0.2, 0.3, 0.2]
harmonic_mean = statistics.harmonic_mean(list_of_numbers, weight)
print("Harmonic_mean is: ")
print(harmonic_mean)

#Hàm median() khi data point là số lẻ:
data = [10, 30, 20, 1000, 50]
median = statistics.median(data)
print("Median: ")
print(median)

#Hàm median() khi data point là số chẳn:
data = [10, 30, 20, 1000, 50, 99]
median = statistics.median(data)
print('Median: ')
print(median)

#Hàm median_low():
data = [10, 30, 20, 40, 50, 60]
median_low = statistics.median_low(data)
print("Median Low is: ")
print(median_low)

#Hàm median_high():
data = [10, 30, 20, 40, 50, 60]
median_high = statistics.median_high(data)
print("Median High is:")
print(median_high)

#Hàm median_grouped():
data = [10, 30, 20, 40, 50, 60, 40, 30, 10]
median_grouped = statistics.median_grouped(data, 2)
print("Median Grouped is: ")
print(median_grouped)

#Hàm mode():
data = [10, 30, 20, 40, 50, 60, 40, 30, 10]
data_string = ["comic", "book","book", "comic", "paper", "comic", "comic"]
result1 = statistics.mode(data)
result2 = statistics.mode(data_string)
print("Mode is: ")
print(result1)
print("Mode with strings are: ")
print(result2)

#Hàm mode khi có nhiều tần số
data = [10, 30, 20, 40, 50, 60, 40, 30, 10, 20, 50, 10, 40]
result1 = statistics.mode(data)
print("Mode is:")
print(result1)

#Hàm multimode():
data = "dddooooooohhhhhhhhh iiiiiii"
result1 = statistics.mode(data)
print("Mode is: ")
print(result1)

#Hàm quantiles():
data = [10, 15, 20, 25, 30, 45, 50, 60, 70, 85, 65]
result = statistics.quantiles(data, n = 4)
print("Quantiles are: ")
print(result)

#Hàm pstdev()
data = [10, 20, 30, 40, 50]
pstdev = statistics.pstdev(data)
print("Pstdev is: ")
print(pstdev)

#Hàm pvariance()
data = [10, 20, 30, 40, 50]
pvariance = statistics.pvariance(data)
print("Pvariance is: ")
print(pvariance)

#Hàm stdev()
data = [10, 20, 30, 40, 50]
stdev = statistics.stdev(data)
print("Stdev is: ")
print(stdev)

#Hàm variance():
data = [10, 20, 30, 40, 50]
variance = statistics.variance(data)
print("Variance is: ")
print(variance)

#Hàm covariance():
x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
covariance = statistics.covariance(x,y)
print("Covariance is: ")
print(covariance)

#Hàm correlation():
x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
correlation = statistics.correlation(x,y)
print("Correlation is: ")
print(correlation)

#Hàm linear_regression
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
result1, result2 = statistics.linear_regression(x,y)
print("Result 1 without proportional is: ", result1)
print("Result 2 without proportional is: ", result2)


















