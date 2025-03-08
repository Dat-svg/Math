import cv2
import numpy as np
import matplotlib.pyplot as plt

# Hàm để tính histogram của ảnh
def compute_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    histogram = histogram / histogram.sum()
    return histogram

# Hàm để tính tích luỹ histogram của ảnh
def compute_cumulative_histogram(histogram):
    cumulative_histogram = histogram.cumsum()
    return cumulative_histogram

# Hàm để áp dụng thuật toán histogram matching
def histogram_matching(input_image, reference_image):
    input_hist = compute_histogram(input_image)
    reference_hist = compute_histogram(reference_image)
    
    input_cdf = compute_cumulative_histogram(input_hist)
    reference_cdf = compute_cumulative_histogram(reference_hist)
    
    mapping = np.interp(input_cdf, reference_cdf, range(256))
    
    matched_image = mapping[input_image]
    
    return matched_image

# Load ảnh gốc và ảnh tham chiếu
input_image = cv2.imread("image3.jpg", cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Áp dụng thuật toán histogram matching
matched_image = histogram_matching(input_image, reference_image)

# Vẽ biểu đồ của ảnh gốc, ảnh tham chiếu và kết quả
plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(input_image, cmap='gray')

plt.subplot(2, 3, 2)
plt.title("References Image")
plt.imshow(reference_image, cmap='gray')

plt.subplot(2, 3, 3)
plt.title("Matched Image")
plt.imshow(matched_image, cmap='gray')

plt.subplot(2, 3, 4)
plt.title("Original Histogram")
plt.hist(input_image.ravel(), 256, [0, 256])
plt.xlabel("Pixel value")

plt.subplot(2, 3, 5)
plt.title("Refenrences Histogram")
plt.hist(reference_image.ravel(), 256, [0, 256])
plt.xlabel("Pixel value")

plt.subplot(2, 3, 6)
plt.title("Matched Histogram")
plt.hist(matched_image.ravel(), 256, [0, 256])
plt.xlabel("Pixel value")

plt.show()

#Lưu ảnh đã cân bằng ra tệp với tên: "matched_image.jpg"
cv2.imwrite("matched_image.jpg", matched_image) 