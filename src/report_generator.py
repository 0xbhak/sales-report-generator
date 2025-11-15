#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul utama untuk generate laporan penjualan
"""

import calendar
from openpyxl import Workbook

from src.data_reader import baca_master_data
from src.sales_generator import generate_produk_random, format_currency
from src.excel_formatter import apply_styling
from src.config import (
    DEFAULT_TARGET_MIN, 
    DEFAULT_TARGET_MAX, 
    DEFAULT_JUMLAH_PRODUK_MIN, 
    DEFAULT_JUMLAH_PRODUK_MAX
)


def generate_laporan_penjualan(file_master, bulan, tahun, store_config, output_dir='.'):
    """
    Generate laporan penjualan untuk satu bulan
    
    Args:
        file_master (str): Path ke file master Excel
        bulan (int): Bulan (1-12)
        tahun (int): Tahun
        store_config (StoreConfig): Konfigurasi toko
        output_dir (str): Direktori output
        
    Returns:
        str: Path ke file output yang telah dibuat
        
    Raises:
        ValueError: Jika parameter tidak valid
    """
    
    # Validasi input
    if not 1 <= bulan <= 12:
        raise ValueError("Bulan harus antara 1-12")
    
    if not store_config.is_complete():
        raise ValueError("Konfigurasi toko belum lengkap!")
    
    # Baca master data
    print("Membaca data file raw master...")
    df_master = baca_master_data(file_master)
    print(f"Total produk di master: {len(df_master)}")
    
    # Dapatkan jumlah hari dalam bulan
    jumlah_hari = calendar.monthrange(tahun, bulan)[1]
    nama_bulan = calendar.month_name[bulan]
    
    print(f"\nMembuat laporan untuk {nama_bulan} {tahun} ({jumlah_hari} hari)\n")
    
    # Buat workbook
    wb = Workbook()
    wb.remove(wb.active)  # Hapus sheet default
    
    # Generate untuk setiap hari
    for hari in range(1, jumlah_hari + 1):
        tanggal = f"{hari:02d}/{bulan:02d}/{tahun}"
        sheet_name = f"{hari:02d}-{bulan:02d}-{tahun}"
        
        print(f"  [{hari:2d}/{jumlah_hari}] Generating {sheet_name}...", end=' ')
        
        # Generate data penjualan
        data_penjualan, total = generate_produk_random(
            df_master,
            target_total_min=DEFAULT_TARGET_MIN,
            target_total_max=DEFAULT_TARGET_MAX,
            jumlah_produk_min=DEFAULT_JUMLAH_PRODUK_MIN,
            jumlah_produk_max=DEFAULT_JUMLAH_PRODUK_MAX
        )
        
        # Buat worksheet
        ws = wb.create_sheet(title=sheet_name)
        
        # Apply styling dan isi data
        apply_styling(ws, data_penjualan, tanggal, total, store_config)
        
        print(f"✓ Total: Rp {format_currency(total)}, Items: {len(data_penjualan)}")
    
    # Simpan file
    output_file = f"{output_dir}/Laporan_Penjualan_{nama_bulan}_{tahun}.xlsx"
    wb.save(output_file)
    print(f"\n{'='*60}")
    print(f"✅ File berhasil dibuat: {output_file}")
    print(f"{'='*60}")
    
    return output_file
