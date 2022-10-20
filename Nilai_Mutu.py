matkul = input("Masukkan matkul : ")
tugas = int(input("Nilai tugas : "))
kuis = int(input("Nilai kuis : "))
uts = int(input("Nilai uts : "))
uas = int(input("Nilai uas : "))

nilai_a = (tugas*0.2)+(kuis*0.3)+(uts*0.2)+(uas*0.3)

if nilai_a >= 85:
  nm = "A"
elif nilai_a >= 78:
  nm = "AB"
elif nilai_a >= 70:
  nm = "B"
elif nilai_a >= 63:
  nm = "BC"
elif nilai_a >= 55:
  nm = "C"
elif nilai_a >= 40:
  nm = "D"
else:
  nm = "E"

print("Mata kuliah : ", matkul)
print("Nilai akhir : ", nilai_a)
print("Nilai Mutu : ", nm)
