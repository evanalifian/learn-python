from variables import subjects, grades

def calculateIPK(dict_user_matkul):
  total_sks = 0
  scores = 0

  for matkul in dict_user_matkul.keys():
    total_sks += subjects[matkul]
    scores += grades[dict_user_matkul[matkul]] * subjects[matkul]

  return scores / total_sks