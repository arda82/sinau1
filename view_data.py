import sqlite3

def lihat_db(nama_db,nama_table):
    """
    Menampilkan semua data dalam tabel database.

    Args:
        nama_db: Nama file database SQLite.

    Returns:
        None.
    """

    try:
        print("")
        # Membuka koneksi ke database
        taut = sqlite3.connect(nama_db)
        cursor = taut.cursor()

        # Menjalankan query untuk mengambil semua data
        cursor.execute(f"SELECT * FROM {nama_table}")

        # Mendapatkan nama kolom
        kolom_nama = [metadata[0] for metadata in cursor.description]
        for kolom in kolom_nama:
                print(f"{kolom} :")
    except sqlite3.Error as e:
        # Menangani kesalahan dan menampilkan pesan error
        print(f"Terjadi kesalahan saat melihat database: {e}")
    
    finally:
        if taut :
            taut.close()
