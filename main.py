#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Laporan Penjualan Toko
Main entry point untuk aplikasi
"""

from src.config import StoreConfig
from src.report_generator import generate_laporan_penjualan


def get_store_info():
    """
    Mendapatkan informasi toko dari user
    
    Returns:
        StoreConfig: Objek konfigurasi toko
    """
    print("\n" + "="*60)
    print("INFORMASI TOKO")
    print("="*60)
    
    nama_toko = input("\nNama Toko: ").strip()
    alamat = input("Alamat: ").strip()
    telepon = input("Nomor Telepon: ").strip()
    
    return StoreConfig(nama_toko, alamat, telepon)


def get_month_input():
    """
    Mendapatkan input bulan dari user
    
    Returns:
        int: Bulan (1-12)
    """
    print("\n" + "="*60)
    print("PILIH BULAN")
    print("="*60)
    print("\nMasukkan bulan (1-12):")
    print("1=Januari, 2=Februari, 3=Maret, 4=April, 5=Mei, 6=Juni,")
    print("7=Juli, 8=Agustus, 9=September, 10=Oktober, 11=November, 12=Desember")
    
    while True:
        try:
            bulan_input = input("\nPilih bulan (1-12): ").strip()
            bulan = int(bulan_input)
            if 1 <= bulan <= 12:
                return bulan
            print("❌ Bulan harus antara 1-12!")
        except ValueError:
            print("❌ Masukkan angka yang valid!")
        except KeyboardInterrupt:
            print("\n\n❌ Dibatalkan.")
            exit(0)


def get_year_input():
    """
    Mendapatkan input tahun dari user
    
    Returns:
        int: Tahun
    """

    while True:
        try:
            tahun_input = input("\nMasukkan tahun (contoh: 2025): ").strip()
            tahun = int(tahun_input)
            if tahun < 2000 or tahun > 2100:
                print("❌ Tahun harus antara 2000-2100!")
                continue
            return tahun
        except ValueError:
            print("❌ Masukkan tahun yang valid!")
        except KeyboardInterrupt:
            print("\n\n❌ Dibatalkan.")
            exit(0)

def get_master_file_path():
    """
    Mendapatkan path file master dari user
    
    Returns:
        str: Path ke file master
    """
    print("\n" + "="*60)
    print("FILE MASTER PRODUK")
    print("="*60)
    print("\nMasukkan path file raw master Excel (atau tekan Enter untuk default 'work-area/bahan.xlsx'):")
    file_master_input = input("Path file master: ").strip()
    
    if not file_master_input:
        return 'work-area/bahan.xlsx'
    return file_master_input


def get_output_directory():
    """
    Mendapatkan direktori output dari user
    
    Returns:
        str: Path ke direktori output
    """
    print("\nMasukkan folder output (atau tekan Enter untuk folder work-area):")
    output_dir_input = input("Folder output: ").strip()
    
    if not output_dir_input:
        return './work-area'
    return output_dir_input


def main():
    """Fungsi utama aplikasi"""
    print("=" * 60)
    print("GENERATOR LAPORAN PENJUALAN TOKO")
    print("="*60)
    print("\nSelamat datang! Aplikasi ini akan membantu Anda")
    print("membuat laporan penjualan bulanan secara otomatis.")
    
    try:
        # 1. Input informasi toko
        store_config = get_store_info()
        
        # Konfirmasi informasi toko
        print(store_config)
        konfirmasi = input("Apakah informasi di atas sudah benar? (Y/n): ").strip().lower() or 'y'
        if konfirmasi != 'y':
            print("\n❌ Dibatalkan. Silakan jalankan kembali program.")
            return
        
        # 2. Input bulan
        bulan = get_month_input()
        
        # 3. Input tahun
        tahun = get_year_input()
        
        # 4. Input file master
        file_master = get_master_file_path()
        
        # 5. Input output directory
        output_dir = get_output_directory()
        
        # Generate laporan
        print("\n" + "=" * 60)
        print("PROSES GENERATE LAPORAN")
        print("=" * 60)
        
        output_file = generate_laporan_penjualan(
            file_master, 
            bulan, 
            tahun, 
            store_config,
            output_dir
        )
        
        print("\n✅ SELESAI! File laporan telah dibuat.")
        print(f"📁 Lokasi: {output_file}")
        print("\nTerima kasih telah menggunakan aplikasi ini!")
        
    except KeyboardInterrupt:
        print("\n\n❌ Program dibatalkan oleh user.")
        exit(0)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nSilakan cek:")
        print("  • File master sudah benar?")
        print("  • Format data sudah sesuai?")
        print("  • Path file sudah valid?")


if __name__ == "__main__":
    main()
