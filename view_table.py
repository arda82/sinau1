import sqlite3
import view_data

def view(nama_db):
    """
    Melihat semua tabel yang ada dalam file database sqlite3
    Args:
        nama_db: Nama database
    """
    # Creating connection
    taut = sqlite3.connect(nama_db)
    cursor = taut.cursor()



    while True:
       # Execute query
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table';")

        # Print a list of all tables
        for table in cursor.fetchall():
            print(table[0])

        print()
      
        # Menampilkan menu pilihan
        print("Pilihan:")
        print("1. Buat tabel")
        print("2. Hapus tabel")
        print("3. Keluar")

        # Meminta pilihan dari pengguna
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            # Meminta nama tabel dari pengguna
          
            nama_tabel = input("Masukkan nama tabel: ")

            # Membuat tabel kosong
            cursor.execute(f"CREATE TABLE {nama_tabel} (id INTEGER PRIMARY KEY AUTOINCREMENT)")
            taut.commit()

            # Meminta daftar kolom dari pengguna
            kolom = input("Masukkan daftar kolom (dipisahkan koma): ")

            # Mengubah string kolom menjadi list
            kolom_list = kolom.strip(",").split(",")

            # Menambahkan kolom untuk setiap entri dalam daftar
            for kolom in kolom_list:
                cursor.execute(f"ALTER TABLE {nama_tabel} ADD COLUMN {kolom} TEXT")
            taut.commit()

            # Menampilkan pesan konfirmasi
            print(f"Tabel {nama_tabel} dalam database {nama_db} berhasil dibuat!")
            print()

        elif pilihan == "2":
            # Meminta nama tabel yang ingin dihapus
            nama_tabel = input("Masukkan nama tabel yang ingin dihapus: ")

            # Menghapus tabel
            cursor.execute(f"DROP TABLE {nama_tabel}")
            taut.commit()

            # Menampilkan pesan konfirmasi
            print(f"Tabel {nama_tabel} berhasil dihapus!")
            print()

        elif pilihan == "3":
            # Keluar dari loop
            break

        else:
            # Pilihan tidak valid
            print("Pilihan tidak valid. Masukkan angka 1-3.")

    # Menutup koneksi database
    taut.close()


# Menjalankan fungsi dengan nama database "alas.db"
#view_data.lihat_db("bumi.db")
view("bumi.db")
