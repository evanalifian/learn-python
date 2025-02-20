def calculateIPK(dict_user_matkul, dict_matkul, dict_nilai):
  total_sks = 0
  total_nilai = 0

  for matkul in dict_user_matkul.keys():
    total_sks += dict_matkul[matkul]
    total_nilai += dict_nilai[dict_user_matkul[matkul]] * dict_matkul[matkul]

  return total_nilai / total_sks