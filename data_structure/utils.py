def displayDictKeys(dictObj):
  text = ""
  no = 1
  for key in dictObj.keys():
    text += f"{no}. {key}\n"
    no += 1
  return text

def displayMatkulDetails(dict_user_matkul, dict_matkul, dict_nilai):
  for matkul in dict_user_matkul.keys():
    print(f"Matkul: {matkul}\nSKS: {dict_matkul[matkul]}\nNilai: {dict_user_matkul[matkul].upper()}/{dict_nilai[dict_user_matkul[matkul]]}")
    print()