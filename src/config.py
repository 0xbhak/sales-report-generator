#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konfigurasi untuk Generator Laporan Penjualan
"""

class StoreConfig:
    """Class untuk menyimpan konfigurasi toko"""
    
    def __init__(self, nama_toko="", alamat="", telepon=""):
        self.nama_toko = nama_toko
        self.alamat = alamat
        self.telepon = telepon
    
    def is_complete(self):
        """Cek apakah semua konfigurasi sudah diisi"""
        return bool(self.nama_toko and self.alamat and self.telepon)
    
    def __str__(self):
        return f"""
Konfigurasi Toko:
- Nama Toko: {self.nama_toko}
- Alamat: {self.alamat}
- Telepon: {self.telepon}
"""


# Default configuration (dapat diubah sesuai kebutuhan)
DEFAULT_TARGET_MIN = 3000000  # Target minimal total penjualan per hari
DEFAULT_TARGET_MAX = 6000000  # Target maksimal total penjualan per hari
DEFAULT_JUMLAH_PRODUK_MIN = 35  # Jumlah minimal produk per hari
DEFAULT_JUMLAH_PRODUK_MAX = 65  # Jumlah maksimal produk per hari
