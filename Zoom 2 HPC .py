### Studi Kasus & Kode

Berdasarkan materi kuliah mengenai analisis data spasial, pemetaan infrastruktur, dan pemrosesan data berbasis lokasi, berikut adalah studi kasus dan implementasi kode Python menggunakan pustaka `pandas` dan `geopandas` untuk analisis spasial sederhana.

#### Studi Kasus: Analisis Jarak Fasilitas Publik dan Klastering Titik Koordinat Infrastruktur Kota

**Latar Belakang:**
Sebuah dinas tata kota ingin menganalisis titik-titik sebaran fasilitas publik (seperti taman, lampu jalan, atau titik aduan masyarakat) berdasarkan koordinat geografis (*latitude* dan *longitude*) untuk menentukan area prioritas pemeliharaan infrastruktur.

**Tujuan Analisis:**
Membuat program Python untuk memproses data koordinat geografis fasilitas, menghitung jarak antar-titik atau pusat keramaian (*centroid*), serta memfilter wilayah berdasarkan kriteria tertentu untuk mendukung pengambilan keputusan berbasis spasial.
"""

import pandas as pd
import numpy as np

# 1. Simulasi Dataset Fasilitas Publik / Titik Koordinat Infrastruktur Kota
data = {
    'facility_id': ['F001', 'F002', 'F003', 'F004', 'F005', 'F006'],
    'facility_type': ['Taman', 'Lampu Jalan', 'Taman', 'Halte', 'Lampu Jalan', 'Taman'],
    'latitude': [-3.8004, -3.7925, -3.8120, -3.7850, -3.8055, -3.7980],
    'longitude': [102.2655, [102.2710, 102.2540, 102.2800, 102.2620, 102.2750]], # (Disesuaikan ke format numerik standar di bawah)
    'maintenance_priority': ['Tinggi', 'Rendah', 'Sedang', 'Tinggi', 'Rendah', 'Sedang']
}

# Perbaikan format data agar konsisten
data_clean = {
    'facility_id': ['F001', 'F002', 'F003', 'F004', 'F005', 'F006'],
    'facility_type': ['Taman', 'Lampu Jalan', 'Taman', 'Halte', 'Lampu Jalan', 'Taman'],
    'latitude': [-3.8004, -3.7925, -3.8120, -3.7850, -3.8055, -3.7980],
    'longitude': [102.2655, 102.2710, 102.2540, 102.2800, 102.2620, 102.2750],
    'maintenance_priority': ['Tinggi', 'Rendah', 'Sedang', 'Tinggi', 'Rendah', 'Sedang']
}

df_facilities = pd.DataFrame(data_clean)

print("--- Data Awal Fasilitas Infrastruktur ---")
print(df_facilities)

# 2. Analisis Sederhana: Filter Berdasarkan Prioritas Pemeliharaan 'Tinggi'
high_priority_df = df_facilities[df_facilities['maintenance_priority'] == 'Tinggi']

print("\n--- Fasilitas dengan Prioritas Pemeliharaan Tinggi ---")
print(high_priority_df[['facility_id', 'facility_type', 'latitude', 'longitude']])

# 3. Menghitung Titik Pusat (Centroid) Sebaran Infrastruktur Kota
centroid_lat = df_facilities['latitude'].mean()
centroid_lon = df_facilities['longitude'].mean()

print(f"\nTitik Pusat (Centroid) Sebaran Fasilitas Kota:")
print(f"Latitude Rata-rata: {centroid_lat:.4f}")
print(f"Longitude Rata-rata: {centroid_lon:.4f}")