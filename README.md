# Proyek Akhir: Prediksi Dropout Mahasiswa untuk EduTech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah meluluskan banyak mahasiswa berprestasi. Namun, salah satu tantangan terbesar yang dihadapi adalah tingginya angka siswa yang tidak menyelesaikan pendidikan alias dropout. Hal ini berdampak negatif terhadap reputasi institusi dan efektivitas proses belajar mengajar.

### Permasalahan Bisnis
- Tingginya angka dropout siswa dari program pendidikan.
- Kurangnya sistem deteksi dini untuk memantau siswa berisiko dropout.
- Tidak adanya visualisasi data yang membantu pengambilan keputusan manajerial.

### Cakupan Proyek
- Melakukan eksplorasi dan analisis deskriptif terhadap data akademik dan demografis mahasiswa.
- Membangun dashboard visual untuk membantu pihak manajemen memonitor faktor risiko dropout.
- Pengembangan model machine learning untuk prediksi kemungkinan mahasiswa dropout.
- Deployment sistem prediksi menggunakan Streamlit.
- Memberikan rekomendasi kebijakan atau tindakan strategis berdasarkan hasil analisis dan model.

### Persiapan

1. Dataset
    - Lokasi: Menggunakan dataset data.csv yang bisa diakses di repositori berikut: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv kemudian disimpan dengan nama data.csv dan setelah dilakukan preprocessing hasilnya digunakan untuk visualisasi di Looker Studio.
    - Deskripsi: Dataset berisi informasi demografis dan informasi mengenai mahasiswa seperti usia saat masuk, gender, beasiswa, kebutuhan khusus, dll. Informasi ini termasuk status dari mahasiswa, apakah mahasiswa keluar (status = 1) atau tidak (status = 0). Dataset ini memiliki data sebanyak 4.424 baris data serta 37 kolom dan tidak terdapat kolom yang memiliki missing value. Selanjutnya akan dilakukan proses preprocessing, Proses preprocessing dilakukan untuk mempersiapkan data agar dapat diolah dan divisualisasikan, guna membantu untuk memahami faktor-faktor yang memengaruhi tingkat dropout mahasiswa.
2. Setup Environment
    * Membuat dan Mengaktifkan Virtual Environment
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
    * Menginstal Semua Dependensi
        - untuk mencegah terjadinya error, kamu harus menginstall dependensi yang ada di file requirements.txt, bisa dijalankan dengan perintah berikut : 
            ```
            pip install -r requirements.txt
            ```
    * Menjalankan Skrip Python (notebook.py)
        - Setelah virtual environment diaktifkan dan dependensi sudah diinstal, bisa menjalankan proyek ini langsung melalui file `notebook.py`. untuk perintah agar proyek bisa dijalankan sebagai berikut : 
            ```
            python notebook.py
            ```
        - Skrip ini akan secara otomatis:
            - Membaca dataset data.csv
            - Melakukan pembersihan dan preprocessing
            - Membangun model prediksi attrition menggunakan Random Forest
            - Menampilkan hasil evaluasi model


## Business Dashboard
Dashboard eksplorasi visual dibuat untuk mengidentifikasi fitur-fitur penting yang berhubungan dengan dropout, seperti:
- Jumlah status mahasiswa → berdasarkan 2 status yaitu dropout dan graduate atau lulus selain enrolled, mahasiswa banyak yang terkena dropout dengan presentase 50.4%. sehingga terdapat beberapa faktor yang mempengaruhi tingkat ini antara lain : 
    - Berdasarkan Umur saat masuk (Age_at_enrollment) → dropout memang tinggi pada umur yang lebih muda, namun bila dilihat perbandingan untuk umur 27 tahun, status mahasiswa kebanyakan didropout. 
    - Berdasarkan beasiswa (Scholarship_holder) → mahasiswa yang tidak menerima beasiswa kebanyakan dropout, hal ini mungkin dipengaruhi oleh biaya pendidikan yang mahal. 
    - Berdasarkan hutang (Debtor) → mahasiswa yang tidak memiliki hutang kebanyakan lulus, namun mahasiswa yang memiliki hutang rentang untuk dropout sehingga Kondisi finansial adalah faktor penting 
    - Berdasarkan Faktor non-akademik seperti Kebutuhan Pendidikan Khusus(Educational_special_needs) → Meskipun jumlahnya kecil, kelompok kebutuhan pendidikan khusus tidak menunjukkan perbedaan signifikan terhadap dropout, tetapi tetap perlu perhatian khusus secara kualitas layanan.
    - Berdasarkan biaya pendidikan yang tidak up-to-date dalam dalam pembayaran biaya kuliah memiliki tingkat dropout yang jauh lebih tinggi. Mahasiswa yang melunasi biaya kuliah tepat waktu memiliki angka kelulusan tinggi. Dibanding dengan Mahasiswa yang menunggak SPP menunjukkan dropout yang jauh lebih tinggi.

![Image](https://github.com/user-attachments/assets/6bc2e443-8779-4780-b08c-b1809745d0ce)

📎 Link dashboard: [https://lookerstudio.google.com/reporting/5eb578ac-8424-41c9-a71d-65595f60b554]


## Menjalankan Sistem Machine Learning
Model RandomForestClassifier digunakan untuk prediksi dropout berdasarkan fitur-fitur terpilih. Model mencapai performa sebagai berikut:

| Accuracy  | Precision | Recall  | F1 Score |
| ------------- | ------------- | ------------- | ------------- |
| 90.36%  | 89.34%  | 85.56%  | 87.41%  |

Model cukup andal dalam mengenali mahasiswa yang berisiko dropout, dengan F1-score >87%, menunjukkan keseimbangan yang baik antara presisi dan recall.

📎 Tutorial dijalankan melalui lokal:
   * pastikan sudah menginstall semua dependensi menggunakan : 
        ```
        pip install -r requirements.txt
        ```
   * jalankan program difile streamlit_app.py
        ```
        streamlit run streamlit_app.py
        ```
   * streamlit otomatis akan berjalan dibrowser
   

📎 Link deploy streamlit: [https://dashboard-college.streamlit.app/]


## Conclusion
Dari hasil analisis, ditemukan beberapa faktor yang memiliki korelasi tinggi terhadap kemungkinan mahasiswa dropout : 
- Umur : mahasiswa yang dropout kemungkinan terjadi pada umur yang sudah tua, kemungkinan dipengaruhi oleh faktor tanggung jawab tambahan (kerja, keluarga).
- Beasiswa : mahasiswa yang dropout kebanyakan tidak menerima beasiswa, sehingga disini kemungkinan dipengaruhi oleh faktor finansial. 
- Hutang : mahasiswa yang dropout rentang memiliki utang,sehingga Kondisi finansial adalah faktor penting 
- Kebutuhan Pendidikan Khusus : tidak menunjukkan perbedaan signifikan terhadap dropout, tetapi tetap perlu perhatian khusus secara kualitas layanan.
- Biaya pendidikan yang tidak up-to-date dalam dalam pembayaran biaya kuliah  : mahasiswa memiliki tingkat dropout yang jauh lebih tinggi, sehingga disini kemungkinan dipengaruhi oleh faktor finansial. 

Dengan adanya proyek ini menunjukkan bahwa machine learning dapat digunakan secara efektif untuk memprediksi kemungkinan mahasiswa akan dropout. Dengan model prediksi yang memiliki akurasi tinggi dan dukungan visualisasi dashboard, pihak manajemen institusi kini memiliki alat bantu untuk:
- Mengidentifikasi mahasiswa berisiko sejak awal
- Meningkatkan kebijakan atau tindakan strategis berdasarkan hasil analisis.

Dashboard yang dibangun memungkinkan manajemen memantau metrik-metrik ini dan mengambil tindakan preventif lebih cepat.

### Rekomendasi Action Items
- Evaluasi Finansial: Tindak lanjuti mahasiswa yang tertinggal dalam pembayaran karena berpotensi tinggi mengalami dropout.
- Program Beasiswa dan Dukungan: Perluas cakupan beasiswa dan pendampingan psikososial bagi mahasiswa berisiko tinggi.