# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Bisnis edutech (*education technology*) adalah bidang usaha yang memanfaatkan teknologi untuk meningkatkan kualitas, efisiensi, dan akses dalam proses belajar-mengajar. Edutech mencakup berbagai layanan seperti *platform* pembelajaran daring (*online learning*), aplikasi belajar, sistem manajemen pembelajaran (LMS), hingga penggunaan AI untuk personalisasi pembelajaran.

### Permasalahan Bisnis

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Cakupan Proyek

#### Tahap Pemahaman Data
- Mengakses data riwayat karyawan yang mengundurkan diri, termasuk detail terkait latar belakang, performa, kepuasan kerja, dan faktor-faktor lainnya.

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
- Model terbaik, misalnya Random Forest, diintegrasikan ke dalam sistem operasional agar dapat digunakan oleh pengguna akhir.

### Persiapan

Sumber data: 
```
https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv
```

Setup environment:
```
conda create --name attretion-analytics python=3.11.12
conda activate attretion-analytics
pip install -r requirements.txt
```

## Business Dashboard

Visualisasi data disajikan melalui dashboard interaktif yang dibangun menggunakan Google Looker Studio. Dashboard ini menyajikan gambaran distribusi data serta memperlihatkan bagaimana berbagai variabel berkontribusi terhadap tingkat attrition. Anda dapat mengakses dashboard tersebut melalui tautan berikut:
```
https://lookerstudio.google.com/u/0/reporting/49c30a44-ecab-474a-9719-b8fa81f381b3/page/doAJF
```

## Conclusion

Berdasarkan dashboard HR yang divisualisasikan menggunakan Google Looker Studio, diketahui bahwa tingkat attrition karyawan mencapai 16.92%, angka yang tergolong cukup tinggi dan memerlukan perhatian. Karyawan yang belum menikah dan sering lembur cenderung memiliki tingkat attrition lebih tinggi, menunjukkan potensi masalah dalam work-life balance. Departemen Research & Development dan Sales menjadi unit dengan tingkat perpindahan tertinggi, serta peran seperti Sales Executive dan Research Scientist juga mendominasi dalam jumlah keluar.

Dari sisi keterlibatan kerja, karyawan dengan Job Involvement level 2 dan 3 paling banyak meninggalkan perusahaan, menandakan bahwa kurangnya keterlibatan dapat menjadi pemicu utama. Selain itu, kepuasan kerja yang rendah dan menengah, serta minimnya promosi dalam 2–3 tahun terakhir juga menjadi faktor signifikan. Karyawan yang mendapatkan kenaikan gaji tahunan di bawah 15% cenderung lebih sering resign, mengindikasikan bahwa penghargaan finansial berpengaruh besar terhadap retensi. Lulusan Bachelor dan Master juga mendominasi jumlah attrition, kemungkinan karena mereka memiliki lebih banyak pilihan karier di luar.

### Rekomendasi Action Items

Sejumlah langkah strategis direkomendasikan untuk dilakukan perusahaan dalam rangka menyelesaikan permasalahan yang ada dan mencapai tujuan yang diinginkan:

- Implementasi program keseimbangan kerja dan hidup bagi karyawan yang sering lembur, terutama yang belum menikah.

- Evaluasi ulang beban kerja dan jalur pengembangan karier di departemen R&D dan Sales untuk meningkatkan retensi.

- Tingkatkan keterlibatan kerja (job involvement) melalui program mentoring, partisipasi proyek strategis, atau peningkatan otonomi kerja.

- Tinjau sistem promosi internal agar lebih transparan dan adil, khususnya bagi karyawan yang telah lama tidak mendapat kenaikan jabatan.

- Reformasi kebijakan kenaikan gaji tahunan, terutama untuk menjaga kepuasan karyawan yang berkinerja baik.

- Buat jalur karier jangka panjang bagi lulusan berpendidikan tinggi agar mereka melihat masa depan di perusahaan.

- Adakan survei rutin terkait kepuasan dan motivasi kerja, dan gunakan hasilnya untuk mendesain kebijakan HR yang responsif.
