# 📊 Generator Laporan Penjualan Toko

Generator otomatis untuk laporan penjualan bulanan dalam format Excel. Aplikasi ini menghasilkan data penjualan dummy yang realistis berdasarkan master data produk.

## ✨ Fitur

- 🏪 **Konfigurasi Toko Fleksibel** - Input manual untuk nama toko, alamat, dan nomor telepon
- 📅 **Laporan Bulanan Lengkap** - Generate laporan untuk satu bulan penuh dengan sheet terpisah untuk setiap hari
- 🎲 **Data Realistis** - Menghasilkan data penjualan random dengan total yang dapat dikontrol (default: Rp 3-6 juta per hari)
- 📦 **Variasi Produk** - Setiap hari memiliki 35-65 produk berbeda yang dipilih secara acak
- 💎 **Format Excel Profesional** - Styling lengkap dengan header, border, dan format angka Indonesia
- 🔧 **Mudah Dikustomisasi** - Struktur kode modular dan terorganisir

## 📋 Fungsi Utama

### 1. Generate Laporan Penjualan

Membuat file Excel berisi laporan penjualan harian untuk satu bulan penuh dengan:

- Header toko (nama, alamat, telepon)
- Tanggal penjualan
- Rincian produk (nama, jumlah, harga satuan, subtotal)
- Total penjualan per hari

### 2. Manajemen Data Master

Membaca dan memproses data master produk dari file Excel yang berisi:

- Nama produk
- Harga satuan

### 3. Randomisasi Penjualan

Menghasilkan data penjualan realistis dengan:

- Jumlah produk random (35-65 item per hari)
- Total penjualan dalam range tertentu (Rp 3-6 juta)
- Distribusi kuantitas berdasarkan harga produk

## 🚀 Instalasi

### Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/username/sales-report-generator.git
   cd sales-report-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Cara Penggunaan

### Persiapan

1. Siapkan file master produk dalam format Excel (.xlsx)
2. File raw master harus memiliki kolom:
   - Nama Produk
   - Harga Satuan

### Menjalankan Aplikasi

```bash
python main.py
```

## ⚙️ Konfigurasi

Anda dapat mengubah konfigurasi default di file `config.py`:

```python
DEFAULT_TARGET_MIN = 3000000        # Target minimal total per hari (Rp)
DEFAULT_TARGET_MAX = 6000000        # Target maksimal total per hari (Rp)
DEFAULT_JUMLAH_PRODUK_MIN = 35      # Minimal produk per hari
DEFAULT_JUMLAH_PRODUK_MAX = 65      # Maksimal produk per hari
```

## 🎯 Contoh Penggunaan

### Contoh: Generate Laporan Bulan Oktober 2025

```bash
$ python main.py

============================================================
GENERATOR LAPORAN PENJUALAN TOKO
============================================================

Selamat datang! Aplikasi ini akan membantu Anda
membuat laporan penjualan bulanan secara otomatis.

============================================================
INFORMASI TOKO
============================================================

Nama Toko: Toko ABC
Alamat: Jl. Merdeka No. 123, Jakarta
Nomor Telepon: 021-12345678

Konfigurasi Toko:
- Nama Toko: Toko ABC
- Alamat: Jl. Merdeka No. 123, Jakarta
- Telepon: 021-12345678

Apakah informasi di atas sudah benar? (y/n): y

============================================================
PILIH BULAN
============================================================

Masukkan bulan (1-12):
1=Januari, 2=Februari, 3=Maret, 4=April, 5=Mei, 6=Juni,
7=Juli, 8=Agustus, 9=September, 10=Oktober, 11=November, 12=Desember

Pilih bulan: 10

Masukkan tahun (contoh: 2025): 2025

============================================================
FILE MASTER PRODUK
============================================================

Masukkan path file raw master Excel (atau tekan Enter untuk default 'bahan.xlsx'):
Path file master:

Masukkan folder output (atau tekan Enter untuk folder saat ini):
Folder output:

============================================================
PROSES GENERATE LAPORAN
============================================================
Membaca data master...
Total produk di master: 150

Membuat laporan untuk October 2025 (31 hari)

  [ 1/31] Generating 01-10-2025... ✓ Total: Rp 4.523.000, Items: 48
  [ 2/31] Generating 02-10-2025... ✓ Total: Rp 5.234.500, Items: 52
  ...
  [31/31] Generating 31-10-2025... ✓ Total: Rp 3.876.200, Items: 41

============================================================
✅ File berhasil dibuat: ./Laporan_Penjualan_October_2025.xlsx
============================================================

✅ SELESAI! File laporan telah dibuat.
📁 Lokasi: ./Laporan_Penjualan_October_2025.xlsx

Terima kasih telah menggunakan aplikasi ini!
```

## 🤝 Kontribusi

Kontribusi selalu diterima! Jika Anda ingin berkontribusi^^

## 📝 Lisensi

Project ini bersifat open source dan tersedia untuk digunakan secara bebas.
Dibuat untuk memudahkan pembuatan laporan penjualan dummy untuk testing dan development.
EDUCATIONAL PURPOSE ONLY.

## 📞 Kontak

Jika ada pertanyaan atau saran, silakan buat issue di repository ini.

---

**Selamat menggunakan! 🎉**
