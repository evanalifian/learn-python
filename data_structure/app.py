"""
Import semua module yang dibutuhkan:
1. Import variables subjects and grades.
2. Import utils untuk keperluan kecil.
"""
from variables import subjects, grades
from utils import display_subjects, display_user_subjects
from controllers import calculateIPK




"""
Membuat variables and menampilkan daftar matkul:
1. Menyimpan jumlah matkul yang diisi oleh user.
2. Membuat variable dict kosong untuk menyimpan daftar matkul yang diisi user.
3. Menampilkan daftar matkul.
"""
total_subjects = int(input("Masukkan jumlah matkul yang ingin dipilih: "))
user_subjects = {}
display_subjects()
print()




"""
Mengisi matkul beserta nilai yang diperoleh dari matkul tersebut:
1. Mengisi matkul + nilai sesuai jumlah matkul yang ingin diisi sebelumnya.
2. Melakukan validasi pada input matkul tersedia pada daftar atau tidak.
3. Melakukan validasi pada input nilai matkul tersedia pada daftar atau tidak.
4. Menampilkan daftar matkul + nilai yang telah diisi oleh user.
"""
for i in range(total_subjects):
  while True:
    subject = input(f"Masukkan nama matkul: ")
    if subject not in subjects.keys():
      print("Matkul yang anda cari tidak ada pada daftar!")
    else:
      break

  while True:
    grade = input(f"Masukkan nilai matkul {subject} (ket: A, B, atau C): ").lower()
    if grade not in grades.keys():
      print("Nilai yang tersedia: A, B, B+, C, C+, D, D+, dan E")
    else:
      break

  user_subjects[subject] = grade

print("\nMatkul yang berhasil dipilih:")
display_user_subjects(user_subjects)




"""
Menghitung IPK
1. Menghitung IPK menggunakan fungsi calculateIPK() yang menerima parameter.
    - Variable dict matkul user
    - Variable dict daftar matkul
    - Variable dict daftar nilai
2. Menampilkan hasil IPK.
"""
ipk_score = calculateIPK(user_subjects)
print(f"\nNilai IPs Anda adalah: {ipk_score}")