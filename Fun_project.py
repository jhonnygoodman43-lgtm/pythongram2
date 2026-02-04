#Install colorama jika gagal
#!/usr/bin/env python3
import os
import json
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# File untuk menyimpan data
NOTES_FILE = "notes.json"
CONTACTS_FILE = "contacts.json"

# ASCII Banner
BANNER = """
██████╗ ███████╗██╗     ██╗ ██████╗████████╗██╗   ██╗███████╗
██╔══██╗██╔════╝██║     ██║██╔════╝╚══██╔══╝██║   ██║██╔════╝
██║  ██║█████╗  ██║     ██║██║        ██║   ██║   ██║███████╗
██║  ██║██╔══╝  ██║     ██║██║        ██║   ██║   ██║╚════██║
██████╔╝███████╗███████╗██║╚██████╗   ██║   ╚██████╔╝███████║
╚═════╝ ╚══════╝╚══════╝╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
"""

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def show_banner():
    """Menampilkan banner dan nama pembuat"""
    clear_screen()
    print(BANNER)
    print(f"                    Created by {Fore.GREEN}Jhonny Goodman{Style.RESET_ALL}")
    print("=" * 70)
    print()

def get_input(prompt="[ DELICTUS ] : "):
    """Mengambil input dari user dengan prompt khusus"""
    return input(prompt)

# ==================== KALKULATOR ====================
def calculator():
    """Fitur kalkulator sederhana"""
    while True:
        show_banner()
        print("=== KALKULATOR ===")
        print("Operasi yang tersedia: +, -, *, /, ** (pangkat), % (modulo)")
        print("Ketik 'back' untuk kembali ke menu utama")
        print()
        
        expression = get_input()
        
        if expression.lower() == 'back':
            break
        
        try:
            result = eval(expression)
            print(f"\nHasil: {result}")
            get_input("\nTekan Enter untuk melanjutkan...")
        except Exception as e:
            print(f"\nError: {e}")
            get_input("\nTekan Enter untuk melanjutkan...")

# ==================== CATATAN ====================
def load_notes():
    """Memuat catatan dari file"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    """Menyimpan catatan ke file"""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

def notes_manager():
    """Fitur manajemen catatan"""
    while True:
        show_banner()
        print("=== CATATAN ===")
        print("1. Lihat semua catatan")
        print("2. Tambah catatan")
        print("3. Hapus catatan")
        print("4. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '1':
            show_banner()
            notes = load_notes()
            if notes:
                print("=== DAFTAR CATATAN ===\n")
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note}")
                    print("-" * 50)
            else:
                print("Tidak ada catatan.")
            get_input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '2':
            show_banner()
            print("=== TAMBAH CATATAN ===")
            print("Ketik catatan Anda (ketik 'done' pada baris baru untuk selesai):")
            print()
            
            lines = []
            while True:
                line = get_input()
                if line.lower() == 'done':
                    break
                lines.append(line)
            
            if lines:
                note = '\n'.join(lines)
                notes = load_notes()
                notes.append(note)
                save_notes(notes)
                print("\nCatatan berhasil disimpan!")
            else:
                print("\nCatatan kosong, tidak disimpan.")
            get_input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '3':
            notes = load_notes()
            if notes:
                show_banner()
                print("=== HAPUS CATATAN ===\n")
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note[:50]}...")
                    print("-" * 50)
                print()
                
                try:
                    index = int(get_input("Nomor catatan yang akan dihapus (0 untuk batal): "))
                    if index > 0 and index <= len(notes):
                        notes.pop(index - 1)
                        save_notes(notes)
                        print("\nCatatan berhasil dihapus!")
                    elif index != 0:
                        print("\nNomor tidak valid!")
                except ValueError:
                    print("\nInput tidak valid!")
                get_input("\nTekan Enter untuk melanjutkan...")
            else:
                show_banner()
                print("Tidak ada catatan untuk dihapus.")
                get_input("\nTekan Enter untuk melanjutkan...")
                
        elif choice == '4':
            break

# ==================== MANAJEMEN KONTAK ====================
def load_contacts():
    """Memuat kontak dari file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    """Menyimpan kontak ke file"""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def contact_manager():
    """Fitur manajemen kontak"""
    while True:
        show_banner()
        print("=== MANAJEMEN KONTAK ===")
        print("1. Lihat semua kontak")
        print("2. Tambah kontak")
        print("3. Cari kontak")
        print("4. Hapus kontak")
        print("5. Kembali")
        print()
        
        choice = get_input()
        
        if choice == '1':
            show_banner()
            contacts = load_contacts()
            if contacts:
                print("=== DAFTAR KONTAK ===\n")
                for idx, contact in enumerate(contacts, 1):
                    print(f"{idx}. Nama  : {contact['nama']}")
                    print(f"   Telepon: {contact['telepon']}")
                    print(f"   Email  : {contact.get('email', '-')}")
                    print("-" * 50)
            else:
                print("Tidak ada kontak.")
            get_input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '2':
            show_banner()
            print("=== TAMBAH KONTAK ===\n")
            
            nama = get_input("Nama    : ")
            telepon = get_input("Telepon : ")
            email = get_input("Email   : ")
            
            if nama and telepon:
                contact = {
                    'nama': nama,
                    'telepon': telepon,
                    'email': email if email else '-'
                }
                contacts = load_contacts()
                contacts.append(contact)
                save_contacts(contacts)
                print("\nKontak berhasil disimpan!")
            else:
                print("\nNama dan telepon harus diisi!")
            get_input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '3':
            show_banner()
            print("=== CARI KONTAK ===\n")
            
            keyword = get_input("Masukkan nama yang dicari: ")
            contacts = load_contacts()
            
            results = [c for c in contacts if keyword.lower() in c['nama'].lower()]
            
            if results:
                print(f"\nDitemukan {len(results)} kontak:\n")
                for idx, contact in enumerate(results, 1):
                    print(f"{idx}. Nama  : {contact['nama']}")
                    print(f"   Telepon: {contact['telepon']}")
                    print(f"   Email  : {contact.get('email', '-')}")
                    print("-" * 50)
            else:
                print("\nTidak ada kontak yang ditemukan.")
            get_input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '4':
            contacts = load_contacts()
            if contacts:
                show_banner()
                print("=== HAPUS KONTAK ===\n")
                for idx, contact in enumerate(contacts, 1):
                    print(f"{idx}. {contact['nama']} - {contact['telepon']}")
                print()
                
                try:
                    index = int(get_input("Nomor kontak yang akan dihapus (0 untuk batal): "))
                    if index > 0 and index <= len(contacts):
                        contacts.pop(index - 1)
                        save_contacts(contacts)
                        print("\nKontak berhasil dihapus!")
                    elif index != 0:
                        print("\nNomor tidak valid!")
                except ValueError:
                    print("\nInput tidak valid!")
                get_input("\nTekan Enter untuk melanjutkan...")
            else:
                show_banner()
                print("Tidak ada kontak untuk dihapus.")
                get_input("\nTekan Enter untuk melanjutkan...")
                
        elif choice == '5':
            break

# ==================== MENU UTAMA ====================
def main():
    """Fungsi utama aplikasi"""
    while True:
        show_banner()
        print("=== MENU UTAMA ===")
        print("1. Kalkulator")
        print("2. Catatan")
        print("3. Manajemen Kontak")
        print("4. Keluar")
        print()
        
        choice = get_input()
        
        if choice == '1':
            calculator()
        elif choice == '2':
            notes_manager()
        elif choice == '3':
            contact_manager()
        elif choice == '4':
            show_banner()
            print("Terima kasih telah menggunakan aplikasi ini!")
            print(f"See you later, {Fore.GREEN}Jhonny Goodman{Style.RESET_ALL}!")
            break
        else:
            print("\nPilihan tidak valid!")
            get_input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
