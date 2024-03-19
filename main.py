import sqlite3
import view_data
import create_tab
import update

def insert_val(nama_db, nama_tabel):
    """
    Memasukkan, mengedit, dan menghapus nilai dalam tabel database.

    Args:
        nama_db: Nama file database SQLite3.
        nama_tabel: Nama tabel yang sudah ada.

    Returns:
        None.
    """
    
    #membuat table jika belum ada
    create_tab.buat_tabel(nama_db,nama_tabel)

    while True:
        # membuat koneksi
        taut = sqlite3.connect(nama_db)
        cursor = taut.cursor()
        
        # Mendapatkan nama kolom
        cursor.execute(f"SELECT * FROM {nama_tabel}")
        kolom_nama = [metadata[0] for metadata in cursor.description]
        
        # Menampilkan semua nilai
        cursor.execute(f"SELECT * FROM {nama_tabel}")
        for row in cursor.fetchall():
            print(f"ID: {row[0]}")
            for i in range(1, len(row)):
                print(f"{kolom_nama[i]}: {row[i]}")
            print()
        # Menampilkan menu pilihan
        print("Pilihan:")
        print("1. Masukkan nilai baru")
        print("2. Edit data")
        print("3. Hapus data")
        print("4. Keluar")

        # Meminta pilihan dari pengguna
        pilihan = input("Masukkan pilihan: ")

        try:
            if pilihan == "1":
                #melihat semua data dalam tabel yang akan diberi nilai
                view_data.lihat_db(nama_db,nama_tabel)
                # Meminta nilai baru
                val = input("Masukkan nilai baru (dipisahkan koma): ")
                values = val.strip(",").split(",")

                # Memastikan jumlah nilai sama dengan jumlah kolom
                if len(values) != len(kolom_nama):
                    print(f"jumlah nilai tidak sama dengan jumlah kolom")

                # Menyiapkan query INSERT
                query = f"INSERT INTO {nama_tabel} ({','.join(kolom_nama)}) VALUES ({','.join('?' for i in range(len(kolom_nama)))})"

                # Menjalankan query dengan nilai
                cursor.execute(query, values)
                taut.commit()

                # Menampilkan pesan konfirmasi
                print("Nilai berhasil ditambahkan!")

            elif pilihan == "2":
                # edit nilai dari sebuah kolom
                edit_val.update_data(nama_db,nama_tabel)

            elif pilihan == "3":
                # Meminta ID nilai yang ingin dihapus
                id_hapus = input("Masukkan ID Data yang ingin dihapus: ")

                # Mendapatkan nilai lama
                cursor.execute(f"SELECT * FROM {nama_tabel} WHERE {kolom_nama[0]} = ?", (id_hapus,))
                nilai_lama = cursor.fetchone()

                if nilai_lama is None:
                    print(f"Data dengan ID {id_hapus} tidak ditemukan")
                    
                else:
                # Menyiapkan query DELETE
                    query = f"DELETE FROM {nama_tabel} WHERE {kolom_nama[0]} = ?"

                    # Menjalankan query dengan nilai
                    cursor.execute(query, (id_hapus,))
                    taut.commit()

                    # Menampilkan pesan konfirmasi
                    print("Data berhasil dihapus")

            elif pilihan == "4":
                # Pilihan lain
                break

            else:
                # Pilihan tidak valid
                print("Pilihan tidak valid. Masukkan angka 1-4.")

        except sqlite3.Error as e:
            # Menangani kesalahan dan menampilkan pesan error
            print("")
            print(f"Terjadi kesalahan: {e}")

        finally:
            # Menutup koneksi database
            if taut:
                taut.close()

if __name__ == "__main__":
    nama_db = "project_0.db"
    nama_tabel = "sawah"
    insert_val(nama_db,nama_tabel)