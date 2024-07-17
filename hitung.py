from datetime import date

def hitung(mulai):
  """
  Program untuk menghitung umur dalam hari.
  Args:
    mulai: Tanggal mulai hitung dengan format tgl,bln,thn
  Returns:
    Jumlah hari dari mulai hitungan sampai hari ini.
  """

  # Cek format tanggal
  try:
    tanggal, bulan, tahun = mulai.split(",")
    date(int(tahun), int(bulan), int(tanggal))
  except ValueError:
    raise ValueError("Format tanggal tidak valid (harus tgl,bln,thn)")

  # Nilai awal hitungan
  nilai_awal = date(int(tahun), int(bulan), int(tanggal))

  # Tanggal hari ini
  hari_ini = date.today()

  # Menghitung hari
  umur_hari = hari_ini - nilai_awal

  return umur_hari.days


