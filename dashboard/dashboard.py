import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("Dashboard Analisis Data - Bagus Sutha")
st.subheader("10 Kategori Produk Dengan Penjualan Tertinggi")

# Baca file CSV
current_dir = os.path.dirname(__file__)
top_10_category = pd.read_csv(os.path.join(current_dir, 'top_10_category.csv'))
sorted_category = top_10_category.sort_values(by='count', ascending=False)

# Visualisasi
plt.figure(figsize=(12, 6))
bars = plt.barh(sorted_category['product_category_name'], sorted_category['count'], color='#66b3ff', edgecolor='black')

# Menambahkan judul dan label
plt.title("Kategori Produk Terlaris", fontsize=16, fontweight='bold')
plt.xlabel("Jumlah", fontsize=14)
plt.ylabel("Kategori Produk", fontsize=14)

# Menampilkan nilai pada setiap bar dengan gap lebih besar
for bar in bars:
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,  # Menambah offset menjadi 2
             f'{bar.get_width()}', va='center', fontsize=10)

# Membuat grid untuk meningkatkan keterbacaan
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Membalik urutan sumbu y
plt.gca().invert_yaxis()

# Menampilkan chart
plt.tight_layout()  # Menyempurnakan tata letak
st.pyplot(plt)

st.subheader("Perbandingan Frekuensi Metode Pembayaran")

# Baca file CSV untuk pembayaran
payment_counts = pd.read_csv(os.path.join(current_dir, 'payment_counts.csv'))

# Visualisasi
# Warna palet
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Membuat pie chart dengan tampilan lebih profesional
plt.figure(figsize=(8, 8))
plt.pie(
    payment_counts['count'],
    labels=payment_counts['method'],
    autopct='%1.2f%%', 
    colors=colors,
    shadow=True,
    startangle=140, 
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Menambahkan judul
plt.title('Perbandingan Metode Pembayaran', fontsize=16, fontweight='bold')

# Menampilkan chart
plt.axis('equal')  # Memastikan chart berbentuk lingkaran sempurna
st.pyplot(plt)

st.subheader("Tren Total Penjualan Setiap Bulan")

# Membaca data dari file CSV
monthly_sales_full = pd.read_csv('monthly_sales_full.csv')

# Mengonversi kolom year_month menjadi tipe datetime
monthly_sales_full['year_month'] = pd.to_datetime(monthly_sales_full['year_month'].astype(str))

# Membuat visualisasi
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales_full['year_month'], monthly_sales_full['total_sales'], marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')

# Mengatur x-ticks untuk menampilkan semua bulan
plt.xticks(monthly_sales_full['year_month'], rotation=45)
plt.xlim(monthly_sales_full['year_month'].min(), monthly_sales_full['year_month'].max())  # Mengatur batas sumbu x

plt.grid(True)
plt.tight_layout()  # Mengatur layout
st.pyplot(plt)