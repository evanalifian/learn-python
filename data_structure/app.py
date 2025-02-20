"""
Import semua module yang dibutuhkan:
1. Import variables sks_matkul and ket_nilai.
2. Import utils untuk keperluan kecil.
"""
from variables import sks_matkul, ket_nilai
from utils import displayDictKeys, displayMatkulDetails
from controllers import calculateIPK




"""
Membuat variables and menampilkan daftar matkul:
1. Menyimpan jumlah matkul yang diisi oleh user.
2. Membuat variable dict kosong untuk menyimpan daftar matkul yang diisi user.
3. Menampilkan daftar matkul.
"""
input_jumlah_matkul = int(input("Masukkan jumlah matkul yang ingin dipilih: "))
user_matkul = {}
print(f"\nDaftar matkul:\n{displayDictKeys(sks_matkul)}")




"""
Mengisi matkul beserta nilai yang diperoleh dari matkul tersebut:
1. Mengisi matkul + nilai sesuai jumlah matkul yang ingin diisi sebelumnya.
2. Melakukan validasi pada input matkul tersedia pada daftar atau tidak.
3. Melakukan validasi pada input nilai matkul tersedia pada daftar atau tidak.
4. Menampilkan daftar matkul + nilai yang telah diisi oleh user.
"""
for i in range(input_jumlah_matkul):
  while True:
    input_matkul = input(f"Masukkan nama matkul: ")
    if input_matkul not in sks_matkul.keys():
      print("Matkul yang anda cari tidak ada pada daftar!")
    else:
      break

  while True:
    input_nilai = input(f"Masukkan nilai matkul {input_matkul} (ket: A, B, atau C): ").lower()
    if input_nilai not in ket_nilai.keys():
      print("Nilai yang tersedia: A, B, B+, C, C+, D, D+, dan E")
    else:
      break

  print()
  user_matkul[input_matkul] = input_nilai

displayMatkulDetails(user_matkul, sks_matkul, ket_nilai)




"""
Menghitung IPK
1. Menghitung IPK menggunakan fungsi calculateIPK() yang menerima parameter.
    - Variable dict matkul user
    - Variable dict daftar matkul
    - Variable dict daftar nilai
2. Menampilkan hasil IPK.
"""
ipk_score = calculateIPK(user_matkul, sks_matkul, ket_nilai)
print(f"\nNilai IP adalah: {ipk_score}")