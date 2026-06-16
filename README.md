# Komputer-Vision-Edge-Detection-
- **Edge Detection** atau Deteksi Tepi adalah teknik matematis untuk menemukan titik-titik dalam gambar di mana intensitas cahayanya berubah secara tajam atau melompat secara drastis (gradien tinggi). Perubahan tajam ini biasanya merupakan batas fisik suatu benda
- **Bagaimana kerjanya?** Menggunakan algoritma atau operator matriks (seperti Sobel, Prewitt, atau Canny) yang digeser ke seluruh piksel gambar untuk mencari perbedaan nilai piksel yang bersebelahan
- **Fungsi Utama:** Menghasilkan garis luar (outline) objek. Ini adalah tulang punggung dari feature extraction. Dengan mengetahui garis tepinya, sistem bisa menebak bentuk ruang benda—apakah itu garis lurus untuk jalur lintasan robot, atau pola sudut tajam untuk membaca marker AR

# Langkah-Langkah
Berikut adalah panduan langkah demi langkah untuk mengubah gambar menjadi edge menggunakan Python di Google Colab. Kita akan menggunakan pustaka **OpenCV**, yang merupakan standar industri untuk Computer Vision.

### 1️⃣ Masuk Google Colab
- Buka browser dan masuk ke Google Colab
- Klik New Notebook untuk membuat lembar kerja baru

### 2️⃣ Unggah Gambar
Sebelum mengeksekusi kode, kita perlu memasukkan gambar ke dalam sistem penyimpanan seperti Google Drive atau Colab. Contoh di sini menggunakan gambar bunga dahlia
<img width="593" height="376" alt="image" src="https://github.com/user-attachments/assets/ebedd707-7581-4e74-b979-140d051e2d54" />

➡️ Setelah mengunggah gambar, lakukan **mount drive** untuk menghubungkan Colab dengan Google Drive milik kalian
<img width="813" height="713" alt="Screenshot (154)" src="https://github.com/user-attachments/assets/3e15c4b5-19de-463c-a7e0-748ce7c357cf" />

### 3️⃣ Mengimport CV
<img width="926" height="332" alt="image" src="https://github.com/user-attachments/assets/e855a52c-2994-45ff-8c78-7c6ae60ee8f3" />

Keterangan :
- Kode pada sel pertama digunakan untuk mengimport pustaka
- Kode pada sel kedua digunakan untuk membaca gambar yang telah diunggah ke Google Drive
  
  : ⚠️ pastikan tempat penyimpanan ("...") sesuai dengan tempat kalian upload
  
  : ⚠️ atau kalian bisa cari gambar kemudian klik titik tiga (⋮) pilih "Copy path", kemudian paste ke ("...")
- Kode pada sel ketiga digunakan menampilkan gambar

### 4️⃣ Mengubah img menjadi Edge
<img width="484" height="350" alt="image" src="https://github.com/user-attachments/assets/5b42b4fc-b634-4c0f-ab3e-74d318d4c046" />

Keterangan :
- Kode pada sel keempat digunakan untuk mendeteksi garis tepi pada gambar menggunakan metode matematika Laplacian untuk menyimpan hasil gambar dalam format 8-bit
