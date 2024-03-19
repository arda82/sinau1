import sqlite3

def update_data(nama_db, nama_tabel):
    """
    Mengupdate data dalam tabel database SQLite.

    Args:
        nama_db: Nama file database SQLite.
        nama_tabel: Nama tabel yang ingin diupdate.

    Returns:
        None.
    """

    try:
        # Membuat koneksi ke database
        taut = sqlite3.connect(nama_db)
        cursor = taut.cursor()

        # Mendapatkan daftar nama kolom
        cursor.execute(f"PRAGMA table_info({nama_tabel})")
        kolom_nama = [kolom[1] for kolom in cursor.fetchall()]

        # Meminta ID data yang ingin diupdate
        id_update = input("Masukkan ID data yang ingin diupdate: ")

        # Mendapatkan nilai lama
        cursor.execute(f"SELECT * FROM {nama_tabel} WHERE id = ?", (id_update,))
        nilai_lama = cursor.fetchone()

        if nilai_lama is None:
            print(f"Data dengan ID {id_update} tidak ditemukan")

        else:
        # Meminta kolom dan nilai baru
            kolom_update = input("Masukkan kolom yang ingin diupdate: ")
            nilai_update = input("Masukkan nilai baru: ")

            # Memastikan kolom yang diupdate ada
            if kolom_update not in kolom_nama:
                print(f"Kolom {kolom_update} tidak ditemukan")

            else:
                # Menyiapkan query UPDATE
                query = f"UPDATE {nama_tabel} SET {kolom_update} = ? WHERE id = ?"

                # Menjalankan query dengan nilai
                cursor.execute(query, (nilai_update, id_update))
                taut.commit()

                # Menampilkan pesan konfirmasi
                print(f"Data dengan ID {id_update} berhasil diupdate!")
                
    except sqlite3.Error as e:
        print (f"terjadi kesalahan {e} ")

    finally:
        if taut :
            taut.close()
    # Menutup koneksi database
    taut.close()

