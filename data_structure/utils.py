from variables import subjects, grades

def display_subjects():
  no = 1
  print("Daftar Mata Kuliah:")
  for key in subjects.keys():
    print(f"{no}. {key}")
    no += 1

def display_user_subjects(user_subjects):
  for subject in user_subjects.keys():
    print(f"Nama\t: {subject}\nSKS\t: {subjects[subject]}\nNilai\t: {user_subjects[subject].upper()}/{grades[user_subjects[subject]]}")
    print()