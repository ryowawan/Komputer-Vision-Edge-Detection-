# 1. Import pustaka yang dibutuhkan
import cv2 as cv

# 2. Membaca file gambar dari lokasi yang kamu tentukan di dalam tanda kutip
img = cv.imread("...")

# 3. Mengimpor fungsi khusus dari Google Colab untuk menampilkan gambar ke layar,
# lalu memanggil fungsi tersebut untuk menampilkan gambar asli yang ada di variabel 'img'.
from google.colab.patches import cv2_imshow
cv2_imshow(img)

# 4. Mendeteksi garis tepi pada gambar menggunakan metode matematika Laplacian agar gambar diproses dan hasil disimpan kedalam format 8-bit
edge = cv.Laplacian(img,cv.CV_8U)
cv2_imshow(edge)
