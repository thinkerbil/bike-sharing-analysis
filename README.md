# 🚲 Capital Bikeshare: Business Performance Dashboard

Dashboard interaktif ini dibuat menggunakan Streamlit untuk menganalisis tren penyewaan sepeda berdasarkan berbagai faktor, seperti cuaca, waktu (jam), dan profil hari (hari kerja vs hari libur).

## 📂 Struktur Proyek
- `dashboard/`: Berisi file utama untuk dashboard (`dashboard.py`, `main_data.csv`, dan aset gambar).
- `data/`: Dataset mentah yang digunakan dalam analisis.
- `notebook.ipynb`: Proses analisis data mulai dari Wrangling, Exploratory Data Analysis (EDA), hingga Visualisasi.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.

## 🛠️ Persiapan Lingkungan (Setup Environment)

### Setup Environment - Anaconda/Conda
```
conda create --name bike-sharing-ds python=3.9
conda activate bike-sharing-ds
pip install -r requirements.txt
```

### Setup Environment - Terminal/Shell
```
cd proyek_analisis_data
python -m venv venv
# Aktivasi venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
# Install library
pip install -r requirements.txt
```

### Run Stremlit App
streamlit run dashboard/dashboard.py

## Link Dashboard (Streamlit Cloud)
Anda juga dapat mengakses versi live dari dashboard ini melalui tautan berikut:
👉 [Dashboard Bike Share Analysis](https://bike-share-analysis-nabila-najwa-husna.streamlit.app/)


