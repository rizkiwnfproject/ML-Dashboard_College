# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan di seluruh Indonesia. Meski telah berkembang pesat, perusahaan mengalami tantangan dalam mempertahankan karyawan. Tercatat, attrition rate (rasio karyawan keluar) telah mencapai lebih dari 10%, yang dapat mempengaruhi produktivitas dan efisiensi perusahaan.

Manajer HR ingin memahami faktor-faktor apa yang menyebabkan tingginya tingkat keluar (attrition) karyawan dan mencari cara untuk mengelolanya lebih baik ke depan.

### Permasalahan Bisnis

- Mengapa banyak karyawan yang keluar dari perusahaan?
- Faktor-faktor apa yang paling berpengaruh terhadap keputusan karyawan untuk resign?

### Cakupan Proyek

- Melakukan data eksplorasi dan analisis terhadap data HR perusahaan.
- Mengidentifikasi faktor-faktor utama yang berkorelasi dengan attrition.
- Membuat business dashboard interaktif untuk HR agar bisa memantau kondisi SDM.
- Membuat model machine learning prediktif untuk memprediksi attrition.
- Memberikan rekomendasi strategis kepada manajemen HR.

### Persiapan Proyek

1. Dataset
    - Lokasi: Menggunakan dataset employee_data.csv yang bisa diakses di repositori berikut: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee kemudian disimpan dengan nama employee_data.csv dan setelah dilakukan preprocessing hasilnya disimpan sebagai employee_data_cleaned.csv dan digunakan untuk visualisasi di Looker Studio.
    - Deskripsi: Dataset berisi informasi demografis dan pekerjaan karyawan, termasuk flag apakah karyawan keluar (attrition = 1) atau tidak (attrition = 0). Dataset ini memiliki data sebanyak 1.470 baris data serta 35 kolom dan terdapat kolom yang memiliki missing value. Selanjutnya akan dilakukan proses preprocessing, Proses preprocessing dilakukan untuk mempersiapkan data agar dapat diolah dan divisualisasikan, guna membantu HR memahami faktor-faktor yang memengaruhi tingkat attrition karyawan.
2. Membuat dan Mengaktifkan Virtual Environment
    - Buka terminal lalu jalankan perintah berikut: 
        ```
        python -m venv venv
        ```
        - kemudian, jika menggunakan windows jalankan : 
            ```
            venv\Scripts\activate
            ```
        - atau jika menggunakan macOS/linux jalankan : 
            ```
            source venv/bin/activate
            ```
3. Menginstal Semua Dependensi
    - untuk mencegah terjadinya error, kamu harus menginstall dependensi yang ada di file requirements.txt, bisa dijalankan dengan perintah berikut : 
        ```
        pip install -r requirements.txt
        ```
4. Menjalankan Skrip Python (notebook.py)
    - Setelah virtual environment diaktifkan dan dependensi sudah diinstal, bisa menjalankan proyek ini langsung melalui file `notebook.py`. untuk perintah agar proyek bisa dijalankan sebagai berikut : 
        ```
        python notebook.py
        ```
    - Skrip ini akan secara otomatis:
        - Membaca dataset employee_data.csv
        - Melakukan pembersihan dan preprocessing
        - Menyimpan hasil ke employee_data_cleaned.csv
        - Membangun model prediksi attrition menggunakan Logistic Regression dan Random Forest
        - Menampilkan hasil evaluasi model

## Business Dashboard

Business dashboard dibuat menggunakan Looker Studio untuk memudahkan manajemen HR dalam memantau:
- Tingkat attrition secara keseluruhan
- Distribusi attrition berdasarkan:
    - Departemen : Keterkaitan antara departemen dengan banyaknya pegawai yang resign
    - Job Role : Keterkaitan antara peran pekerjaan dengan banyaknya pegawai yang resign
    - Job Satisfaction : Keterkaitan antara kenyamanan bekerja dengan banyaknya pegawai yang resign
    - Range Overtime : Keterkaitan antara waktu lembur dengan banyaknya pegawai yang resign
    - Perbandingan antara karyawan yang bertahan dan yang keluar

![Image](https://github.com/user-attachments/assets/4450f8b7-1ae4-4de2-9c5e-bbb8b3d1cfcd)

📎 Link dashboard: [https://lookerstudio.google.com/reporting/33ae4310-b288-408e-9c72-fe0ec15a332e]

## Conclusion

Dari hasil analisis, ditemukan beberapa faktor yang memiliki korelasi tinggi terhadap kemungkinan karyawan keluar:

- Departemen : Karyawan dari departemen Research dan development cenderung lebih banyak yang resign, disusul dengan departemen sales. hal ini kemungkinan dikarenakan beban kerja yang terlalu banyak. Sehingga untuk mengatasinya mungkin dapat merekrut pegawai lagi untuk lebih menyetabilkan beban kerja antara karyawan satu dengan yang lain. 
- OverTime: Karyawan yang sering lembur memiliki tingkat attrition lebih tinggi dari pada karyawan yang tidak lembur. Sehingga untuk mengatasinya mungkin dapat diberikan kompensasi ketika lembur atau membatasi jam kerja sehingga tidak sampai lembur.
- Job Satisfaction : Karyawan dengan kenyamanan bekerja yang rendah cenderung lebih mudah resign. Hal ini mungkin berhubungan dengan overtime, sehingga untuk mengatasinya mungkin dapat diberikan fasilitas untuk menunjang kenyamanan dalam bekerja. 
- Job Role: Laboratory Technican dan sales cenderung lebih mudah untuk resign mungkin dikarenakan beban kerja yang cukup berat. 

Dashboard yang dibangun memungkinkan HR memantau metrik-metrik ini dan mengambil tindakan preventif lebih cepat.