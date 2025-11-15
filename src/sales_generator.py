#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul untuk generate data penjualan random
"""

import random


def generate_produk_random(df_master, target_total_min=3000000, target_total_max=6000000, 
                          jumlah_produk_min=35, jumlah_produk_max=65):
    """
    Generate daftar produk random dengan total dalam range yang ditentukan
    
    Args:
        df_master (pd.DataFrame): DataFrame master produk
        target_total_min (int): Target minimal total penjualan
        target_total_max (int): Target maksimal total penjualan
        jumlah_produk_min (int): Jumlah minimal produk
        jumlah_produk_max (int): Jumlah maksimal produk
        
    Returns:
        tuple: (data_penjualan, total)
            - data_penjualan (list): List of dict berisi data penjualan
            - total (int): Total penjualan
    """
    
    max_attempts = 100
    for attempt in range(max_attempts):
        # Random jumlah produk
        jumlah_produk = random.randint(jumlah_produk_min, jumlah_produk_max)
        
        # Pilih produk random (tanpa duplikasi)
        if len(df_master) < jumlah_produk:
            selected_indices = random.sample(range(len(df_master)), len(df_master))
        else:
            selected_indices = random.sample(range(len(df_master)), jumlah_produk)
        
        data_penjualan = []
        total = 0
        
        for idx in selected_indices:
            produk = df_master.iloc[idx]
            harga_satuan = int(produk['Harga Satuan'])
            
            # Generate jumlah item (lebih banyak untuk produk murah, lebih sedikit untuk produk mahal)
            if harga_satuan < 10000:
                jumlah = random.randint(1, 50)
            elif harga_satuan < 50000:
                jumlah = random.randint(1, 20)
            else:
                jumlah = random.randint(1, 10)
            
            sub_total = jumlah * harga_satuan
            total += sub_total
            
            data_penjualan.append({
                'Nama Produk': produk['Nama Produk'],
                'Jumlah': jumlah,
                'Harga Satuan': harga_satuan,
                'Sub Total': sub_total
            })
        
        # Cek apakah total dalam range yang diinginkan
        if target_total_min <= total <= target_total_max:
            return data_penjualan, total
        
        # Jika total terlalu kecil, tambah jumlah pada beberapa item
        if total < target_total_min:
            adjustment_needed = target_total_min - total
            for _ in range(min(5, len(data_penjualan))):
                item = random.choice(data_penjualan)
                if item['Harga Satuan'] > 0:
                    additional = max(1, adjustment_needed // (item['Harga Satuan'] * 5))
                    item['Jumlah'] += additional
                    item['Sub Total'] = item['Jumlah'] * item['Harga Satuan']
            
            total = sum(item['Sub Total'] for item in data_penjualan)
            if target_total_min <= total <= target_total_max:
                return data_penjualan, total
        
        # Jika total terlalu besar, kurangi jumlah pada beberapa item
        elif total > target_total_max:
            adjustment_needed = total - target_total_max
            for _ in range(min(5, len(data_penjualan))):
                item = random.choice(data_penjualan)
                if item['Jumlah'] > 1 and item['Harga Satuan'] > 0:
                    reduction = min(item['Jumlah'] - 1, adjustment_needed // item['Harga Satuan'])
                    item['Jumlah'] -= reduction
                    item['Sub Total'] = item['Jumlah'] * item['Harga Satuan']
            
            total = sum(item['Sub Total'] for item in data_penjualan)
            if target_total_min <= total <= target_total_max:
                return data_penjualan, total
    
    # Jika setelah max attempts masih belum sesuai, return yang terakhir
    return data_penjualan, total


def format_currency(value):
    """
    Format angka menjadi format currency Indonesia
    
    Args:
        value (int/float): Nilai yang akan diformat
        
    Returns:
        str: String terformat dengan pemisah ribuan (.)
    """
    return f"{int(value):,}".replace(',', '.')
