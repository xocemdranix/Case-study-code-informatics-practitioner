### Studi Kasus & Kode

Berdasarkan materi kuliah mengenai visualisasi data, analisis interaktif, dan prinsip penyajian informasi yang bersih serta informatif, berikut adalah studi kasus dan implementasi kode Python menggunakan pustaka `pandas` dan `matplotlib` untuk menganalisis dan memvisualisasikan data metrik kinerja atau tren operasional secara efektif.

#### Studi Kasus: Visualisasi Kinerja Penjualan Bulanan dan Analisis Tren untuk Dasbor Eksekutif

**Latar Belakang:**
Sebuah perusahaan ritel ingin menyajikan ringkasan data kinerja penjualan bulanan kepada para pengambil keputusan (*executive summary*). Sesuai prinsip visualisasi data yang baik (menghindari *chartjunk* dan menyajikan informasi dengan cepat), data penjualan perlu diolah dan divisualisasikan dalam bentuk grafik batang dan garis yang bersih serta mudah dipahami dalam waktu singkat.

**Tujuan Analisis:**
Membuat program Python untuk memproses data penjualan bulanan, menghitung total metrik utama, serta menghasilkan visualisasi grafik interaktif/statis yang bersih untuk mendukung dasbor analitik perusahaan.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulasi Dataset Kinerja Penjualan Bulanan
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'Total_Penjualan_Juta': [120, 135, 150, 142, 160, 175, 190, 185, 210, 225, 240, 280],
    'Jumlah_Transaksi': [1100, 1250, 1400, 1320, 1500, 1650, 1800, 1750, 1950, 2100, 2250, 2600]
}

df_sales = pd.DataFrame(data)

print("--- Ringkasan Data Penjualan ---")
print(df_sales.to_string(index=False))

# 2. Analisis Statistik Dasar untuk Dasbor
total_sales_year = df_sales['Total_Penjualan_Juta'].sum()
avg_sales_month = df_sales['Total_Penjualan_Juta'].mean()

print(f"\nTotal Penjualan Tahun Ini: Rp {total_sales_year} Juta")
print(f"Rata-rata Penjualan Bulanan: Rp {avg_sales_month:.2f} Juta")

# 3. Visualisasi Data yang Bersih dan Profesional (Clean & Minimalist Design)
plt.figure(figsize=(10, 5))

# Membuat Line & Bar Chart kombinasi sederhana untuk tren
plt.plot(df_sales['Bulan'], df_sales['Total_Penjualan_Juta'], color='#1f77b4', marker='o', linewidth=2.5, label='Tren Penjualan (Juta IDR)')

plt.title('Tren Kinerja Penjualan Bulanan Perusahaan', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Bulan', fontsize=11)
plt.ylabel('Penjualan (Dalam Juta IDR)', fontsize=11)

# Mengatur grid agar tipis dan rapi (mengurangi clutter / chartjunk)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

# Menyesuaikan tata letak agar estetis
plt.tight_layout()

# Menampilkan grafik visualisasi
plt.show()