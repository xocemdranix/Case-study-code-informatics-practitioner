### Studi Kasus & Kode Berbasis Python

Berdasarkan materi kuliah mengenai pemrosesan data spasial, analisis citra satelit, dan klasifikasi pemicu perubahan penampakan lahan, berikut adalah studi kasus dan implementasi kode Python menggunakan pustaka `pandas` dan `scikit-learn` untuk mengklasifikasikan jenis pemicu deforestasi berdasarkan fitur spasial numerik.

#### Studi Kasus: Klasifikasi Pemicu Deforestasi Menggunakan Model *Machine Learning* Berbasis Data Satelit

**Latar Belakang:**
Sebuah lembaga riset lingkungan ingin membangun model prediktif berbasis kecerdasan buatan untuk mengklasifikasikan penyebab utama dari titik-titik peringatan hilangnya tutupan pohon (*deforestation alerts*) yang terdeteksi oleh satelit. Fitur yang dianalisis meliputi luas area gangguan, indeks pantulan radar, keberadaan titik panas (*hotspot* kebakaran), dan jarak ke jalan terdekat.

**Tujuan Analisis:**
Membuat program Python untuk melatih model klasifikasi (menggunakan *Random Forest*) guna mengidentifikasi apakah suatu area mengalami deforestasi akibat pertanian, pertambangan, pembalakan liar, atau kebakaran hutan.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Simulasi Dataset Peringatan Deforestasi & Fitur Spasial
data = {
    'alert_size_ha': [1.2, 15.5, 0.8, 45.0, 2.5, 30.1, 0.5, 12.0, 50.2, 1.0],
    'radar_backscatter_change': [0.15, 0.85, 0.20, 0.90, 0.30, 0.88, 0.10, 0.75, 0.95, 0.18],
    'fire_hotspot_detected': [0, 1, 0, 0, 0, 1, 0, 0, 1, 0], # 0: Tidak ada, 1: Ada
    'distance_to_road_km': [0.5, 3.2, 0.2, 8.5, 1.0, 5.0, 0.1, 2.5, 10.0, 0.4],
    'deforestation_driver': [
        'Pertanian Kecil', 'Pertanian Besar', 'Pembalakan Liar', 'Pertanian Besar',
        'Pembalakan Liar', 'Kebakaran Hutan', 'Pembalakan Liar', 'Pertanian Besar',
        'Pertanian Besar', 'Pertanian Kecil'
    ]
}

df_deforest = pd.DataFrame(data)

print("--- Contoh Data Latens / Fitur Spasial ---")
print(df_deforest.head())

# 2. Menentukan Variabel Fitur (X) dan Target (y)
X = df_deforest[['alert_size_ha', 'radar_backscatter_change', 'fire_hotspot_detected', 'distance_to_road_km']]
y = df_deforest['deforestation_driver']

# 3. Membagi Data Menjadi Training (80%) dan Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Melatih Model Menggunakan Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 5. Evaluasi Performa Model pada Data Uji (Testing Set)
y_pred = rf_model.predict(X_test)

print("\n--- Evaluasi Model Klasifikasi Pemicu Deforestasi ---")
print(f"Akurasi Model: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred, zero_division=0))