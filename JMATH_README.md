# J MATH TOOLKIT
Aplikasi Matematika Lengkap oleh Jhonny Goodman

## Fitur

### 1. **Operasi Dasar**
   - Penjumlahan (+)
   - Pengurangan (−)
   - Perkalian (×)
   - Pembagian (÷)

### 2. **Pangkat & Akar**
   - Pangkat (a^b)
   - Akar kuadrat (√)
   - Akar pangkat n

### 3. **Faktorial**
   - Menghitung faktorial (n!)
   - Mendukung bilangan hingga 100

### 4. **FPB & KPK**
   - FPB (Faktor Persekutuan Terbesar)
   - KPK (Kelipatan Persekutuan Terkecil)

### 5. **Bilangan Prima**
   - Cek apakah bilangan prima
   - Daftar bilangan prima dari 1 sampai n

### 6. **Persamaan Linear**
   - Menyelesaikan persamaan ax + b = 0

### 7. **Statistik**
   - Menghitung rata-rata (mean)
   - Menghitung median

## Instalasi

### Untuk Linux/Termux

1. **Install Python 3** (jika belum terinstall)
   ```bash
   # Untuk Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Untuk Termux
   pkg update
   pkg install python
   ```

2. **Install library colorama**
   ```bash
   pip install colorama --break-system-packages
   
   # Atau untuk Termux
   pip install colorama
   ```

3. **Download file jmath_toolkit.py**

4. **Berikan izin eksekusi**
   ```bash
   chmod +x jmath_toolkit.py
   ```

## Cara Menjalankan

### Metode 1 (Langsung)
```bash
python3 jmath_toolkit.py
```

### Metode 2 (Executable)
```bash
./jmath_toolkit.py
```

## Panduan Penggunaan

### Login
- Saat pertama kali menjalankan, Anda akan diminta memasukkan username
- Username tidak boleh kosong
- Username akan ditampilkan di setiap halaman

### Navigasi
- Gunakan angka untuk memilih menu
- Input prompt: `>>>`
- Setiap fungsi/menu ditampilkan dengan warna biru
- Hasil perhitungan ditampilkan dengan warna cyan

### Tips Penggunaan

**Operasi Dasar:**
- Pilih operasi yang diinginkan
- Masukkan dua angka
- Hasil akan ditampilkan

**Faktorial:**
- Masukkan bilangan bulat positif
- Maksimal nilai: 100

**Bilangan Prima:**
- Untuk daftar prima, maksimal nilai: 1000
- Semakin besar nilai, semakin lama proses

**Statistik:**
- Masukkan data dipisahkan dengan spasi
- Contoh: 10 20 30 40 50

**Persamaan Linear:**
- Masukkan nilai a dan b
- Program akan menyelesaikan ax + b = 0

## Fitur Khusus

- ✅ **Banner ASCII "J Math"** dengan warna merah
- ✅ **Nama creator** (Jhonny Goodman) dengan warna hijau
- ✅ **Fungsi menu** dengan warna biru
- ✅ **Sistem login** dengan username
- ✅ **Interface yang clean** dan mudah digunakan

## Contoh Penggunaan

### Menghitung FPB
```
Masukkan bilangan pertama: 48
Masukkan bilangan kedua: 18
FPB dari 48 dan 18 = 6
```

### Menghitung Median
```
Data: 5 10 15 20 25
Jumlah data: 5
Rata-rata: 15.0
Median: 15.0
```

### Cek Bilangan Prima
```
Masukkan bilangan: 17
17 adalah bilangan prima!
```

## Troubleshooting

**Error: colorama not found**
```bash
pip install colorama --break-system-packages
```

**Permission denied**
```bash
chmod +x jmath_toolkit.py
```

**Karakter ASCII tidak muncul dengan benar**
- Pastikan terminal mendukung UTF-8
- Gunakan terminal emulator yang mendukung Unicode

## Catatan

- Aplikasi ini menggunakan library `math` (built-in Python)
- Semua data tidak disimpan (session based)
- Untuk keluar, pilih "Logout" dari menu utama

## Kredit
Created by Jhonny Goodman

---
**Version:** 1.0  
**Last Updated:** 2026
