import sqlite3

def buat_tabel(nama_db, nama_tabel):
    """
    Membuat tabel A dalam database SQLite jika belum ada.

    Args:
        nama_db: Nama file database SQLite.
        nama_tabel: Nama tabel yang ingin dibuat.

    Returns:
        None.
    """

    # Membuat koneksi ke database
    try :
        taut = sqlite3.connect(nama_db)
        cursor = taut.cursor()

        # Menjalankan query untuk mendapatkan nama semua tabel
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        # Mengecek apakah nama_tabel ada dalam daftar nama tabel
        tabel_ada = False
        for table in cursor.fetchall():
            if table[0] == nama_tabel:
                tabel_ada = True
                break

        # Jika tabel tidak ada, buat tabel baru
        if not tabel_ada:
            query = f"CREATE TABLE {nama_tabel}(id INTEGER PRIMARY KEY AUTOINCREMENT)"
            cursor.execute(query)
            taut.commit()

            print(f"Tabel {nama_tabel} berhasil dibuat!")

            kolom = input("Masukkan daftar kolom (dipisahkan koma): ")

            # Mengubah string kolom menjadi list
            kolom_list = kolom.strip(",").split(",")

            # Menambahkan kolom untuk setiap entri dalam daftar
            for kolom in kolom_list:
                cursor.execute(f"ALTER TABLE {nama_tabel} ADD COLUMN {kolom} TEXT")
            taut.commit()

            print(f"Kolom baru telah ditambahkan ke tabel {nama_tabel}.")
            
    except sqlite3.Error as e:
          #menangani kesalahan dan menampilkan pesan error
        print (f"terjadi  kesalahan: {e}")
            
    finally :
        if taut:
            taut.close()
