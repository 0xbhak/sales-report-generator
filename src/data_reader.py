#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul untuk membaca dan memproses data master produk
"""

import pandas as pd


def baca_master_data(file_path):
    """
    Membaca data master produk dari file excel
    
    Args:
        file_path (str): Path ke file excel master
        
    Returns:
        pd.DataFrame: DataFrame berisi Nama Produk dan Harga Satuan
        
    Raises:
        ValueError: Jika header tidak ditemukan atau file tidak valid
        FileNotFoundError: Jika file tidak ditemukan
    """
    try:
        df = pd.read_excel(file_path, header=None)
    except FileNotFoundError:
        raise FileNotFoundError(f"File master '{file_path}' tidak ditemukan!")
    except Exception as e:
        raise ValueError(f"Error membaca file raw master: {e}")
    
    # Cari baris header (yang berisi "Nama Produk")
    header_row = None
    for idx, row in df.iterrows():
        if 'Nama Produk' in str(row.values):
            header_row = idx
            break
    
    if header_row is None:
        raise ValueError("Header 'Nama Produk' tidak ditemukan dalam file master!")
    
    # Ambil data mulai dari baris setelah header
    df_clean = df.iloc[header_row + 1:].copy()
    df_clean.columns = ['No', 'Nama Produk', 'Harga Satuan']
    
    # Bersihkan data
    df_clean = df_clean.dropna(subset=['Nama Produk', 'Harga Satuan'])
    df_clean['Harga Satuan'] = pd.to_numeric(df_clean['Harga Satuan'], errors='coerce')
    df_clean = df_clean.dropna(subset=['Harga Satuan'])
    df_clean = df_clean[df_clean['Harga Satuan'] > 0]  # Filter harga > 0
    
    # Reset index
    df_clean = df_clean.reset_index(drop=True)
    
    result = df_clean[['Nama Produk', 'Harga Satuan']]
    
    if len(result) == 0:
        raise ValueError("Tidak ada data produk valid dalam file raw master!")
    
    return result
