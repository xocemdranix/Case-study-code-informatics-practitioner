### Studi Kasus & Kode

Berdasarkan materi kuliah mengenai alur kerja *Supervised Learning* (khususnya *Classification*), berikut adalah studi kasus dan implementasi kode Python menggunakan pustaka `scikit-learn` untuk memprediksi kelayakan persetujuan pinjaman berdasarkan data nasabah.

#### Studi Kasus: Prediksi Kelayakan Persetujuan Pinjaman (*Loan Approval Prediction*)

**Latar Belakang:**
Sebuah lembaga keuangan ingin mengotomatisasi proses evaluasi pengajuan pinjaman nasabah guna mempercepat pengambilan keputusan dan mengurangi risiko kredit macet. Berdasarkan data historis nasabah, sistem *Machine Learning* dilatih untuk mengklasifikasikan apakah pengajuan pinjaman layak disetujui atau ditolak.

**Tujuan Analisis:**
Membangun model klasifikasi menggunakan algoritma *Decision Tree* di Python untuk memprediksi status persetujuan pinjaman berdasarkan fitur seperti nilai kredit (*credit score*), rasio utang (*debt ratio*), dan status pekerjaan.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Simulasi Dataset Historis Pengajuan Pinjaman
data = {
    'credit_score': [720, 580, 650, 490, 780, 610, 800, 530, 690, 710],
    'debt_ratio': [0.2, 0.6, 0.4, 0.8, 0.1, 0.5, 0.15, 0.7, 0.3, 0.25],
    'employment_status': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], # 1: Tetap/Aktif, 0: Tidak Tetap
    'loan_approved': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]     # Target: 1 (Disetujui), 0 (Ditolak)
}

df = pd.DataFrame(data)

print("--- Contoh Data Laten ---")
print(df.head())

# 2. Menentukan Fitur (X) dan Target (y)
X = df[['credit_score', 'debt_ratio', 'employment_status']]
y = df['loan_approved']

# 3. Membagi Data Menjadi Training (80%) dan Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Melatih Model Menggunakan Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Melakukan Evaluasi pada Data Testing (Unseen Data)
y_pred = model.predict(X_test)

print("\n--- Evaluasi Performa Model ---")
print(f"Akurasi Model: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred, zero_division=0))