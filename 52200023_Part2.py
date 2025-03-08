import cv2
import numpy as np
import matplotlib.pyplot as plt

def hist_equalization(img):
    # Tính toán lược đồ histogram
    hist = np.zeros(256, dtype= int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1

    # Tính toán CDF
    cdf = np.zeros(256, dtype = int) 
    cdf = np.cumsum(hist) / hist.sum()

    # Giá trị pixel và tạo mảng để lưu ảnh đã cân bằng
    equalized_img = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            value_new = cdf[img[i, j]] * 255
            equalized_img[i, j] = value_new

    return equalized_img

if __name__ == "__main__":
    # Đọc ảnh image
    img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

    # Điều chỉnh lại kích thước image
    img = cv2.resize(img, (640, 480))

    # Áp dụng thuật toán histogram equalization
    equalized_img = hist_equalization(img)

    # Lưu ảnh đã cân bằng ra tệp "equalized_image.jpg"
    cv2.imwrite("equalized_image.jpg", equalized_img)


    #Tính lược đồ tần số cho ảnh gốc và ảnh đã cân bằng
    old_hist = cv2.calcHist([img], [0], None, [256], [0,256])
    hist_equalized = cv2.calcHist([equalized_img], [0], None, [256], [0,256])

    # Hiện thị ảnh
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")

    plt.subplot(2, 2, 2)
    plt.imshow(equalized_img, cmap="gray")
    plt.title("Equalized Image")

    # Lược đồ nguyên bản
    plt.subplot(2, 2, 3)
    plt.plot(old_hist, color = 'blue')
    plt.title("Original Histogram")
    plt.xlabel("Pixel value")
    plt.ylabel("Frequency")

    # Lược đồ đã điều chỉnh
    plt.subplot(2, 2, 4)
    plt.plot(hist_equalized, color = 'green')
    plt.title("Equalized Histogram")
    plt.xlabel("Pixel value")
    plt.ylabel("Cumulative frequency")

    plt.tight_layout()
    plt.show()