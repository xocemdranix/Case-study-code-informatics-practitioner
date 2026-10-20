# Informatics Practitioner Lecture Series
Repositori ini berisi rangkuman materi, studi kasus, dan implementasi kode Python dari 6 sesi **Informatics Practitioner Lecture Series** yang menghubungkan pengetahuan akademik dengan aplikasi industri dan teknologi global.

---

## Daftar Materi & Pembahasan

### 1. Make Sense of Data with Analysis and AI
* **Pemateri:** Andria Arisal (Peneliti BRIN)
* **Topik Utama:**
  * Metodologi CRISP-DM dan hirarki pengolahan data: *Data $\rightarrow$ Information $\rightarrow$ Insight $\rightarrow$ Decision*.
  * Empat level analisis: *Descriptive*, *Diagnostic*, *Predictive*, dan *Prescriptive*.
  * Pemanfaatan *workflow analytics* (KNIME) dan integrasi Generative AI dalam *data preparation*.

### 2. Bridging Global Infrastructure to Address Local Challenge with HPC
* **Pemateri:** Asst. Prof. Dr. Warawan Diaz Carbalo (Thammasat University, Thailand)
* **Topik Utama:**
  * Peran *High Performance Computing* (HPC) dan superkomputer dalam menyelesaikan masalah lokal (iklim, bencana, dan kesehatan).
  * Peran lulusan Informatika sebagai *Integrator* yang menghubungkan domain spesifik dengan infrastruktur komputasi terdistribusi.

### 3. Career and Competition in Industrial Era with GIS
* **Pemateri:** Widi Primadepa, S.Kom. (Asset Management GIS Analyst di City Care Property, Selandia Baru)
* **Topik Utama:**
  * Keunggulan lulusan Teknik Informatika dalam dunia GIS melalui penguasaan pemrograman, basis data spasial (PostGIS), dan otomatisasi alur kerja.
  * Penerapan GIS internasional (ArcGIS Enterprise, QGIS, FME) untuk *smart cities* dan manajemen aset infrastruktur.

### 4. Introduction to Machine Learning
* **Pemateri:** Dr. Taniza Tajudin
* **Topik Utama:**
  * Konsep dasar *Machine Learning* (ML) sebagai bagian dari *Artificial Intelligence* (AI).
  * Taksonomi ML: *Supervised*, *Unsupervised*, *Reinforcement*, dan *Semi-Supervised Learning*.
  * Alur kerja ML, evaluasi model, serta tantangan etika dan transparansi (*Explainable AI*).

### 5. Human-Computer Interaction & Data Visualization
* **Pemateri:** Dr. Arafat Febriandirza, S.T., M.T. (Ketua Kelompok Riset HCI & Visualisasi, BRIN)
* **Topik Utama:**
  * Prinsip *User-Centered Design* (UCD), psikologi kognitif, dan pengelolaan *cognitive load*.
  * Teknik visualisasi data efektif: peningkatan *data-ink ratio*, eliminasi *chartjunk*, dan visualisasi interaktif.

### 6. Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI
* **Pemateri:** Dr. Bart Slachter (Wageningen University and Research, Belanda)
* **Topik Utama:**
  * Penggabungan citra satelit radar (Sentinel-1) dan optik (Sentinel-2) untuk menembus tutupan awan di wilayah tropis.
  * Penggunaan *Convolutional Neural Network* (CNN) untuk mengklasifikasikan pemicu langsung deforestasi secara otomatis.

---

##  Studi Kasus & Implementasi Kode Python

Repositori ini mencakup implementasi Python untuk berbagai skenario analitis:

1. **Prediksi Keterlambatan Pembayaran Invoice (CRISP-DM):**
   * Klasifikasi potensi *late payment* menggunakan `RandomForestClassifier`.
2. **Simulasi Konsumsi Energi Gedung Berbasis Agen (HPC/Simulation):**
   * Pemodelan aktivitas harian penghuni gedung dan estimasi energi.
3. **Analisis Titik Koordinat Infrastruktur Kota (GIS):**
   * Pengolahan data spasial, filter prioritas pemeliharaan, dan perhitungan *centroid*.
4. **Prediksi Kelayakan Pinjaman / Loan Approval (Machine Learning):**
   * Klasifikasi kelayakan pinjaman nasabah menggunakan `DecisionTreeClassifier`.
5. **Visualisasi Kinerja Penjualan Bulanan (HCI & Data Viz):**
   * Penyajian tren data minimalis dan profesional menggunakan `matplotlib`.
6. **Klasifikasi Pemicu Deforestasi Berbasis Data Satelit (Remote Sensing & AI):**
   * Pemodelan multi-fitur spasial untuk deteksi penyebab kerusakan hutan.

---

## ⚙️ Cara Menjalankan Kode

1. **Clone Repositori:**
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Instal Pustaka Dependensi:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```

3. **Jalankan Skrip Python:**
   ```bash
   python script_name.py
   ```
