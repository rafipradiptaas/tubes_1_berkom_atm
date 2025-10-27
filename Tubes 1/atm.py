#ATM kami
#tes_push_1
# SIMULASI ATM SEDERHANA TANPA FUNGSI
#=============================
# KAMUS GLOBAL
# =============================
# pin_list      : list of string  - menyimpan PIN pengguna
# nama_list     : list of string  - menyimpan nama pengguna
# norek_list    : list of string  - menyimpan nomor rekening
# saldo_list    : list of int     - menyimpan saldo pengguna
# riwayat_list  : list of list    - menyimpan riwayat transaksi
# user_index    : int             - index user yang sedang login
# max_attempts  : int             - maksimal percobaan login

# Deklarasi Variabel  
pin_list = ["123456", "654321"]
nama_list = ["Jonathan Lewie", "Rafi Pradipta"]
norek_list = ["19625126", "19625122"]
saldo_list = [5000000, 3000000]
riwayat_list = [[], []]

print("\n" * 50)
print("=" * 60)
print("\n")
print("██████╗  █████╗ ███╗   ██╗██╗  ██╗    ███████╗".center(60))
print("██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ╚════██║".center(60))
print("██████╔╝███████║██╔██╗ ██║█████╔╝         ██╔╝".center(60))
print("██╔══██╗██╔══██║██║╚██╗██║██╔═██╗        ██╔╝ ".center(60))
print("██████╔╝██║  ██║██║ ╚████║██║  ██╗       ██║  ".center(60))
print("╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝  ".center(60))
print("\n")
print("--Automated Teller Machine--".center(60))
print("Layanan 24/7".center(60))
print("=" * 60)
print()

# =======================
# LOGIN
# =======================
max_attempts = 3
attempts = 0
user_index = -1

while attempts < max_attempts:
    print("=" * 60)
    print("SISTEM LOGIN".center(60))
    print("=" * 60)
    print(f"Percobaan ke-{attempts + 1} dari {max_attempts}")
    print()
    pin = input("Masukkan PIN (6 digit): ")

    found = False
    for i in range(len(pin_list)):
        if pin_list[i] == pin:
            found = True
            user_index = i
            break

    if found:
        print("\n" * 50)
        print("=" * 60)
        print("LOGIN BERHASIL!".center(60))
        print("=" * 60)
        print(f"Selamat datang, {nama_list[user_index]}!".center(60))
        input("\nTekan Enter untuk melanjutkan...")
        break
    else:
        attempts += 1
        sisa = max_attempts - attempts
        if sisa > 0:
            print("\nPIN salah! Sisa percobaan:", sisa)
            input("Tekan Enter untuk coba lagi...")
        else:
            print("\nAkses ditolak. PIN salah 3 kali.")
            print("Sistem keluar otomatis.")
            exit()

# =======================
# MENU UTAMA
# =======================
while True:
    print("\n" * 50)
    print("=" * 60)
    print("INFORMASI AKUN".center(60))
    print("=" * 60)
    print(f"Pemegang Kartu : {nama_list[user_index]}")
    print(f"No. Rekening   : {norek_list[user_index]}")
    print(f"Saldo Tersedia : Rp {saldo_list[user_index]:,}".replace(",", "."))
    print("=" * 60)
    print()
    print("MENU UTAMA".center(60))
    print("=" * 60)
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Transfer")
    print("5. Riwayat Transaksi")
    print("6. Keluar")
    print("=" * 60)

    pilihan = input("Pilihan Anda (1-6): ")
    print("\n")

    # =======================
    # CEK SALDO
    # =======================
    if pilihan == "1":
        print("=" * 60)
        print("CEK SALDO".center(60))
        print("=" * 60)
        print(f"Nama Pemilik   : {nama_list[user_index]}")
        print(f"Nomor Rekening : {norek_list[user_index]}")
        print(f"Saldo Tersedia : Rp {saldo_list[user_index]:,}".replace(",", "."))
        print("=" * 60)
        input("Tekan Enter untuk kembali...")

    # =======================
    # TARIK TUNAI
    # =======================
    elif pilihan == "2":
        print("=" * 60)
        print("TARIK TUNAI".center(60))
        print("=" * 60)
        print(f"Saldo Anda: Rp {saldo_list[user_index]:,}".replace(",", "."))
        print("\nNominal harus kelipatan Rp 50.000")
        jumlah_str = input("Masukkan jumlah penarikan (Rp): ")

        if not jumlah_str.isdigit():
            print("\nERROR: Input harus angka!")
        else:
            jumlah = int(jumlah_str)
            if jumlah <= 0:
                print("ERROR: Jumlah harus lebih dari 0!")
            elif jumlah % 50000 != 0:
                print("ERROR: Jumlah harus kelipatan Rp 50.000!")
            elif jumlah > saldo_list[user_index]:
                print("ERROR: Saldo tidak mencukupi!")
            else:
                saldo_list[user_index] -= jumlah
                riwayat_list[user_index].append(f"Tarik Tunai|{jumlah}")
                print("\nTRANSAKSI BERHASIL!")
                print(f"Jumlah: Rp {jumlah:,}".replace(",", "."))
                print(f"Saldo Akhir: Rp {saldo_list[user_index]:,}".replace(",", "."))
        input("\nTekan Enter untuk kembali...")

    # =======================
    # SETOR TUNAI
    # =======================
    elif pilihan == "3":
        print("=" * 60)
        print("SETOR TUNAI".center(60))
        print("=" * 60)
        jumlah_str = input("Masukkan jumlah setoran (Rp): ")
        if not jumlah_str.isdigit():
            print("\nERROR: Input harus angka!")
        else:
            jumlah = int(jumlah_str)
            if jumlah <= 0:
                print("ERROR: Jumlah harus lebih dari 0!")
            else:
                saldo_list[user_index] += jumlah
                riwayat_list[user_index].append(f"Setor Tunai|{jumlah}")
                print("\nSETORAN BERHASIL!")
                print(f"Jumlah: Rp {jumlah:,}".replace(",", "."))
                print(f"Saldo Akhir: Rp {saldo_list[user_index]:,}".replace(",", "."))
        input("\nTekan Enter untuk kembali...")

    # =======================
    # TRANSFER
    # =======================
    elif pilihan == "4":
        print("=" * 60)
        print("TRANSFER ANTAR REKENING".center(60))
        print("=" * 60)
        print(f"Saldo Anda: Rp {saldo_list[user_index]:,}".replace(",", "."))
        no_rek_tujuan = input("Masukkan nomor rekening tujuan: ")

        if no_rek_tujuan not in norek_list:
            print("\nERROR: Rekening tidak ditemukan!")
            input("Tekan Enter untuk kembali...")
        else:
            index_tujuan = norek_list.index(no_rek_tujuan)
            if index_tujuan == user_index:
                print("\nERROR: Tidak bisa transfer ke rekening sendiri!")
                input("Tekan Enter untuk kembali...")
            else:
                print(f"Nama Penerima: {nama_list[index_tujuan]}")
                jumlah_str = input("Masukkan jumlah transfer (Rp): ")
                if not jumlah_str.isdigit():
                    print("\nERROR: Input harus angka!")
                else:
                    jumlah = int(jumlah_str)
                    if jumlah <= 0:
                        print("ERROR: Jumlah harus lebih dari 0!")
                    elif jumlah > saldo_list[user_index]:
                        print("ERROR: Saldo tidak mencukupi!")
                    else:
                        konfirmasi = input("Lanjutkan transfer? (y/n): ")
                        if konfirmasi.lower() == "y":
                            saldo_list[user_index] -= jumlah
                            saldo_list[index_tujuan] += jumlah
                            riwayat_list[user_index].append(f"Transfer ke {nama_list[index_tujuan]}|{jumlah}")
                            print("\nTRANSFER BERHASIL!")
                            print(f"Penerima: {nama_list[index_tujuan]}")
                            print(f"Jumlah: Rp {jumlah:,}".replace(",", "."))
                            print(f"Saldo Akhir: Rp {saldo_list[user_index]:,}".replace(",", "."))
                        else:
                            print("\nTransfer dibatalkan.")
                input("\nTekan Enter untuk kembali...")

    # =======================
    # RIWAYAT TRANSAKSI
    # =======================
    elif pilihan == "5":
        print("=" * 60)
        print("RIWAYAT TRANSAKSI".center(60))
        print("=" * 60)
        riwayat = riwayat_list[user_index]
        if len(riwayat) == 0:
            print("Belum ada transaksi.".center(60))
        else:
            for idx, transaksi in enumerate(reversed(riwayat[-10:]), start=1):
                jenis, jumlah = transaksi.split("|")
                print(f"{idx}. {jenis}")
                print(f"   Jumlah: Rp {int(jumlah):,}".replace(",", "."))
        print("=" * 60)
        input("Tekan Enter untuk kembali...")

    # =======================
    # KELUAR
    # =======================
    elif pilihan == "6":
        print("\n" * 50)
        print("=" * 60)
        print("Terima kasih telah menggunakan ".center(60))
        print("\n")
        print("██████╗  █████╗ ███╗   ██╗██╗  ██╗    ███████╗".center(60))
        print("██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ╚════██║".center(60))
        print("██████╔╝███████║██╔██╗ ██║█████╔╝         ██╔╝".center(60))
        print("██╔══██╗██╔══██║██║╚██╗██║██╔═██╗        ██╔╝ ".center(60))
        print("██████╔╝██║  ██║██║ ╚████║██║  ██╗       ██║  ".center(60))
        print("╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝  ".center(60))
        print("\n")
        print("Jaga keamanan PIN Anda".center(60))
        print("=" * 60)
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")