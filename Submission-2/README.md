# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Bisnis edutech (*education technology*) adalah bidang usaha yang memanfaatkan teknologi untuk meningkatkan kualitas, efisiensi, dan akses dalam proses belajar-mengajar. Edutech mencakup berbagai layanan seperti *platform* pembelajaran daring (*online learning*), aplikasi belajar, sistem manajemen pembelajaran (LMS), hingga penggunaan AI untuk personalisasi pembelajaran.

### Permasalahan Bisnis
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
#### Tahap Pemahaman Data
- Mengakses data historis terkait profil siswa seperti capaian akademik dan faktor-faktor lain yang berkaitan.

- Menganalisis struktur dan karakteristik data untuk mengenali pola umum yang muncul.

#### Tahap Persiapan Data
- Membersihkan data dari duplikasi dan nilai yang hilang untuk memastikan kualitas data yang optimal.

- Melakukan konversi data kategorikal, normalisasi nilai numerik, serta seleksi fitur yang relevan.

- Mengidentifikasi hubungan antar fitur melalui analisis korelasi.

#### Pembangunan Model Pembelajaran Mesin
- Dataset dibagi menjadi bagian pelatihan dan pengujian.

- Beberapa algoritma dilatih menggunakan data pelatihan untuk memprediksi kemungkinan attrition berdasarkan fitur yang tersedia.

- Parameter model disesuaikan dan performanya diuji melalui proses validasi.

#### Evaluasi Model
- Kinerja model diukur dengan menggunakan metrik seperti akurasi, presisi, recall, dan F1-score, berdasarkan data pengujian.

#### Implementasi
- Mencari model terbaik dari tiga model yang akan diuji yaitu Logistic Regression, Decision Tree, dan Random Forest. Kemudian melakukan integrasi ke dalam sistem operasional agar dapat digunakan oleh pengguna akhir.


### Persiapan

Sumber data: 
```
https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv
```

Setup environment:
```
conda create --name students-performance python=3.11.12
conda activate students-performance
pip install -r requirements.txt
```

## Business Dashboard
Visualisasi data disajikan melalui dashboard interaktif yang dibangun menggunakan Google Looker Studio. Dashboard ini menyajikan gambaran distribusi data serta memperlihatkan bagaimana berbagai variabel berkontribusi terhadap tingkat attrition. Anda dapat mengakses dashboard tersebut melalui tautan berikut:
```
https://lookerstudio.google.com/reporting/6f5fb664-e2e3-41f3-b152-074e527658d3
```

## Menjalankan Sistem Machine Learning
Prototipe sistem Machine Learning ini dikembangkan menggunakan Streamlit dan dapat diakses melalui tautan berikut:

```
https://jaya-jaya-students-performance.streamlit.app/
```
Berikut adalah langkah-langkah untuk menjalankan aplikasinya:

1. Isi formulir dengan data mahasiswa, seperti biaya pendidikan (*Tuition Fees*), status beasiswa (*Scholarship Holder*), jenis kelamin (*Gender*), jadwal kehadiran (*Attendance*), dan informasi lainnya.

2. Setelah semua data terisi, klik tombol *"Click Here to Predict"*.

3. Hasil prediksi akan ditampilkan di bawah tombol, menunjukkan apakah mahasiswa tersebut diprediksi akan lulus (*Graduate*) atau *Drop Out*.

## Conclusion
Berdasarkan visualisasi pada Jaya Jaya Edutech Students Dashboard, dapat disimpulkan bahwa tingkat dropout siswa masih cukup tinggi, yaitu sebesar 39,15% dari total 3.630 siswa. Mayoritas siswa yang terdaftar adalah laki-laki (65,6%) dan sebagian besar mengikuti kelas pada waktu siang (88,9%), sedangkan kelas malam hanya diikuti oleh sebagian kecil siswa. Sebaran gender juga menunjukkan dominasi laki-laki di kedua sesi waktu, terutama pada kelas siang. Lebih dari separuh siswa berasal dari latar belakang terdampak atau displaced, namun sebagian besar siswa tidak mendapatkan beasiswa, yang menunjukkan masih terbatasnya akses terhadap bantuan finansial. Sebagian besar siswa juga tidak memiliki pinjaman pendidikan. 

Dari sisi usia, mayoritas siswa mendaftar pada usia 53–57 tahun, mengindikasikan bahwa institusi ini lebih banyak melayani kelompok usia dewasa. Sementara itu, distribusi siswa berdasarkan urutan aplikasi menunjukkan bahwa mereka yang mendaftar lebih awal (order 0 dan 1) cenderung memiliki tingkat kelulusan yang lebih tinggi. Kursus yang paling banyak diminati berada di rentang kode 9500–9700. Temuan-temuan ini menunjukkan perlunya peningkatan dukungan finansial, akses pendidikan yang lebih merata, serta strategi khusus untuk menurunkan angka dropout dan meningkatkan keberhasilan siswa.

### Rekomendasi Action Items
Sejumlah langkah strategis direkomendasikan untuk dilakukan perusahaan dalam rangka menyelesaikan permasalahan yang ada dan mencapai tujuan yang diinginkan:
- Tindak lanjuti dengan survei atau wawancara pada siswa dropout.

- Evaluasi kebijakan pemberian beasiswa agar lebih banyak siswa bisa terbantu, terutama dari kelompok displaced dan non-debtor.

- Pertimbangkan beasiswa berbasis kebutuhan daripada hanya prestasi.

- Tingkatkan fasilitas atau fleksibilitas bagi peserta di kelas malam (misalnya: materi online, tutor tambahan), mengingat kelompok ini jumlahnya kecil dan mungkin butuh dukungan ekstra.

- Buat program pemberdayaan dan promosi untuk meningkatkan partisipasi siswa perempuan, khususnya untuk program STEM.

- Jika ingin meningkatkan kelulusan jangka panjang, arahkan promosi pada kelompok usia lebih muda (misal usia 20–30), karena usia saat ini didominasi 50-an.

- Beri insentif atau kemudahan bagi siswa yang mendaftar lebih awal (application order 0 atau 1), karena tren menunjukkan mereka lebih mungkin berhasil menyelesaikan studi.
