#!/usr/bin/env python3
import os
import math
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Global variable untuk username
current_user = ""

# ASCII Banner J Math
BANNER = f"""{Fore.RED}
     ██╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
     ██║    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
     ██║    ██╔████╔██║███████║   ██║   ███████║
██   ██║    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
╚█████╔╝    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
 ╚════╝     ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
{Style.RESET_ALL}"""

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def show_banner():
    """Menampilkan banner"""
    clear_screen()
    print(BANNER)
    print(f"                    Created by {Fore.GREEN}Jhonny Goodman{Style.RESET_ALL}")
    print("=" * 70)
    print()

def get_input(prompt=">>> "):
    """Mengambil input dari user"""
    return input(prompt)

def print_func(text):
    """Print dengan warna biru untuk nama fungsi"""
    print(f"{Fore.BLUE}{text}{Style.RESET_ALL}")

# ==================== LOGIN ====================
def login():
    """Sistem login sederhana"""
    global current_user
    show_banner()
    print("=== LOGIN ===")
    print()
    username = get_input("Masukkan username Anda: ")
    
    if username.strip():
        current_user = username.strip()
        print(f"\nSelamat datang, {Fore.GREEN}{current_user}{Style.RESET_ALL}!")
        get_input("\nTekan Enter untuk melanjutkan...")
        return True
    else:
        print("\nUsername tidak boleh kosong!")
        get_input("\nTekan Enter untuk mencoba lagi...")
        return False

# ==================== OPERASI DASAR ====================
def operasi_dasar():
    """Kalkulator operasi dasar"""
    while True:
        show_banner()
        print_func("=== OPERASI DASAR ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (−)")
        print("3. Perkalian (×)")
        print("4. Pembagian (÷)")
        print("5. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '5':
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                a = float(get_input("Masukkan angka pertama: "))
                b = float(get_input("Masukkan angka kedua: "))
                
                if choice == '1':
                    result = a + b
                    print(f"\n{a} + {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                elif choice == '2':
                    result = a - b
                    print(f"\n{a} − {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                elif choice == '3':
                    result = a * b
                    print(f"\n{a} × {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                elif choice == '4':
                    if b != 0:
                        result = a / b
                        print(f"\n{a} ÷ {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                    else:
                        print("\nError: Tidak bisa dibagi dengan nol!")
                
                get_input("\nTekan Enter untuk melanjutkan...")
            except ValueError:
                print("\nError: Input harus berupa angka!")
                get_input("\nTekan Enter untuk melanjutkan...")
        else:
            print("\nPilihan tidak valid!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== PANGKAT & AKAR ====================
def pangkat_akar():
    """Operasi pangkat dan akar"""
    while True:
        show_banner()
        print_func("=== PANGKAT & AKAR ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("1. Pangkat (a^b)")
        print("2. Akar Kuadrat (√)")
        print("3. Akar Pangkat n")
        print("4. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '4':
            break
        
        try:
            if choice == '1':
                a = float(get_input("Masukkan bilangan: "))
                b = float(get_input("Masukkan pangkat: "))
                result = a ** b
                print(f"\n{a}^{b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                get_input("\nTekan Enter untuk melanjutkan...")
                
            elif choice == '2':
                a = float(get_input("Masukkan bilangan: "))
                if a >= 0:
                    result = math.sqrt(a)
                    print(f"\n√{a} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                else:
                    print("\nError: Tidak bisa menghitung akar dari bilangan negatif!")
                get_input("\nTekan Enter untuk melanjutkan...")
                
            elif choice == '3':
                a = float(get_input("Masukkan bilangan: "))
                n = float(get_input("Masukkan akar ke-: "))
                if n != 0:
                    result = a ** (1/n)
                    print(f"\n{a}^(1/{n}) = {Fore.CYAN}{result}{Style.RESET_ALL}")
                else:
                    print("\nError: Akar tidak boleh nol!")
                get_input("\nTekan Enter untuk melanjutkan...")
            else:
                print("\nPilihan tidak valid!")
                get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Input harus berupa angka!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== FAKTORIAL ====================
def faktorial():
    """Menghitung faktorial"""
    while True:
        show_banner()
        print_func("=== FAKTORIAL ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("Faktorial (n!) = n × (n-1) × (n-2) × ... × 1")
        print("Ketik 'back' untuk kembali")
        print()
        
        n = get_input("Masukkan bilangan bulat positif: ")
        
        if n.lower() == 'back':
            break
        
        try:
            n = int(n)
            if n < 0:
                print("\nError: Faktorial hanya untuk bilangan bulat positif!")
            elif n > 100:
                print("\nError: Angka terlalu besar (max 100)!")
            else:
                result = math.factorial(n)
                print(f"\n{n}! = {Fore.CYAN}{result}{Style.RESET_ALL}")
            get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Input harus berupa bilangan bulat!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== FPB & KPK ====================
def fpb_kpk():
    """Menghitung FPB dan KPK"""
    while True:
        show_banner()
        print_func("=== FPB & KPK ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("1. FPB (Faktor Persekutuan Terbesar)")
        print("2. KPK (Kelipatan Persekutuan Terkecil)")
        print("3. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '3':
            break
        
        try:
            a = int(get_input("Masukkan bilangan pertama: "))
            b = int(get_input("Masukkan bilangan kedua: "))
            
            if a <= 0 or b <= 0:
                print("\nError: Bilangan harus positif!")
                get_input("\nTekan Enter untuk melanjutkan...")
                continue
            
            if choice == '1':
                result = math.gcd(a, b)
                print(f"\nFPB dari {a} dan {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                get_input("\nTekan Enter untuk melanjutkan...")
                
            elif choice == '2':
                result = abs(a * b) // math.gcd(a, b)
                print(f"\nKPK dari {a} dan {b} = {Fore.CYAN}{result}{Style.RESET_ALL}")
                get_input("\nTekan Enter untuk melanjutkan...")
            else:
                print("\nPilihan tidak valid!")
                get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Input harus berupa bilangan bulat!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== BILANGAN PRIMA ====================
def is_prime(n):
    """Cek apakah bilangan prima"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def bilangan_prima():
    """Operasi bilangan prima"""
    while True:
        show_banner()
        print_func("=== BILANGAN PRIMA ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("1. Cek bilangan prima")
        print("2. Daftar bilangan prima (1 sampai n)")
        print("3. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '3':
            break
        
        try:
            if choice == '1':
                n = int(get_input("Masukkan bilangan: "))
                if is_prime(n):
                    print(f"\n{Fore.CYAN}{n}{Style.RESET_ALL} adalah bilangan prima!")
                else:
                    print(f"\n{Fore.CYAN}{n}{Style.RESET_ALL} bukan bilangan prima.")
                get_input("\nTekan Enter untuk melanjutkan...")
                
            elif choice == '2':
                n = int(get_input("Masukkan batas atas (max 1000): "))
                if n > 1000:
                    print("\nError: Batas maksimal adalah 1000!")
                    get_input("\nTekan Enter untuk melanjutkan...")
                    continue
                
                primes = [i for i in range(2, n+1) if is_prime(i)]
                print(f"\nBilangan prima dari 1 sampai {n}:")
                print(f"{Fore.CYAN}{primes}{Style.RESET_ALL}")
                print(f"\nTotal: {len(primes)} bilangan prima")
                get_input("\nTekan Enter untuk melanjutkan...")
            else:
                print("\nPilihan tidak valid!")
                get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Input harus berupa bilangan bulat!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== PERSAMAAN LINEAR ====================
def persamaan_linear():
    """Menyelesaikan persamaan linear ax + b = 0"""
    while True:
        show_banner()
        print_func("=== PERSAMAAN LINEAR ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("Menyelesaikan persamaan: ax + b = 0")
        print("Ketik 'back' untuk kembali")
        print()
        
        a_input = get_input("Masukkan nilai a: ")
        
        if a_input.lower() == 'back':
            break
        
        try:
            a = float(a_input)
            b = float(get_input("Masukkan nilai b: "))
            
            if a == 0:
                if b == 0:
                    print("\nSemua nilai x adalah solusi (0 = 0)")
                else:
                    print("\nTidak ada solusi (persamaan kontradiksi)")
            else:
                x = -b / a
                print(f"\nPersamaan: {a}x + {b} = 0")
                print(f"Solusi: x = {Fore.CYAN}{x}{Style.RESET_ALL}")
            
            get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Input harus berupa angka!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== STATISTIK ====================
def statistik():
    """Menghitung rata-rata dan median"""
    while True:
        show_banner()
        print_func("=== RATA-RATA & MEDIAN ===")
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print("Masukkan data (pisahkan dengan spasi)")
        print("Contoh: 5 10 15 20 25")
        print("Ketik 'back' untuk kembali")
        print()
        
        data_input = get_input("Data: ")
        
        if data_input.lower() == 'back':
            break
        
        try:
            data = [float(x) for x in data_input.split()]
            
            if not data:
                print("\nError: Data tidak boleh kosong!")
                get_input("\nTekan Enter untuk melanjutkan...")
                continue
            
            # Rata-rata
            mean = sum(data) / len(data)
            
            # Median
            sorted_data = sorted(data)
            n = len(sorted_data)
            if n % 2 == 0:
                median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
            else:
                median = sorted_data[n//2]
            
            print(f"\nData: {data}")
            print(f"Jumlah data: {len(data)}")
            print(f"Rata-rata: {Fore.CYAN}{mean}{Style.RESET_ALL}")
            print(f"Median: {Fore.CYAN}{median}{Style.RESET_ALL}")
            
            get_input("\nTekan Enter untuk melanjutkan...")
        except ValueError:
            print("\nError: Semua input harus berupa angka!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== MENU UTAMA ====================
def main_menu():
    """Menu utama aplikasi"""
    while True:
        show_banner()
        print(f"User: {Fore.GREEN}{current_user}{Style.RESET_ALL}")
        print()
        print_func("=== MENU UTAMA ===")
        print()
        print("1. Operasi Dasar (+ − × ÷)")
        print("2. Pangkat & Akar")
        print("3. Faktorial")
        print("4. FPB & KPK")
        print("5. Bilangan Prima")
        print("6. Persamaan Linear")
        print("7. Rata-rata & Median")
        print("8. Logout")
        print()
        
        choice = get_input()
        
        if choice == '1':
            operasi_dasar()
        elif choice == '2':
            pangkat_akar()
        elif choice == '3':
            faktorial()
        elif choice == '4':
            fpb_kpk()
        elif choice == '5':
            bilangan_prima()
        elif choice == '6':
            persamaan_linear()
        elif choice == '7':
            statistik()
        elif choice == '8':
            show_banner()
            print(f"Terima kasih telah menggunakan J Math, {Fore.GREEN}{current_user}{Style.RESET_ALL}!")
            print("Sampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid!")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== MAIN ====================
def main():
    """Fungsi utama"""
    while True:
        if login():
            main_menu()
            break

if __name__ == "__main__":
    main()
