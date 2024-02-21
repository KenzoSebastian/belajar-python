# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++++++3---------------------10++++++++++++++

inputuser = float(input('masukan angka yang bernilai kurang dari 3\natau\nlebih dari 10  = '))

# ++++++++++++3----------------
# memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3)
print('kurang dari 3 = ',iskurangdari)

# ------------------10++++++++++++++++
# memeriksa angka kurang dari 3
islebihdari = (inputuser > 10)
print('lebih dari 10 = ',islebihdari)

# +++++++++++3---------------------10++++++++++++++
# pakai or (|)
iscorrect = iskurangdari | islebihdari
print('angka yang anda masukan = ',iscorrect)


# -------------3++++++++++++++10----------------
# kasus irisan

print("\n===================\n")
inputuser = float(input('masukan angka yang bernilai lebih dari 3\ndan\nkurang dari 10  = '))

# -------------3++++++++++++++++++
# lebih  dari 3

islebihdari = (inputuser > 3)
print("lebih dari 3 = ",islebihdari)

# ++++++++++++++++10-------------
# kurang dari 10

iskurangdari = (inputuser < 10)
print("kurang dari 10 = ",iskurangdari)

# -------------3++++++++++++++10----------------
# pakai and (&)
iscorrect = islebihdari & iskurangdari
print("nilai yang anda masukan = ",iscorrect)


# PR KELAS TERBUKA
print("\n============PR KELAS TERBUKA================\n")

# No.1. ------0++++++5-------8+++++++11--------
print("No 1. ------0++++++5-------8+++++++11--------\n")
inputuser = float(input("Masukan angka diantara 0 sampai 5 atau angka\ndiantara 8 sampai 11 = "))
print ("\n===========HASIL===========\n")

# ----------0+++++++++++++++
# memeriksa angka lebih dari 0
lebihdari = inputuser > 0
print("lebih dari 0 = ", lebihdari)

# +++++++++5---------------
# memeriksa angka kurang dari 5
kurangdari = inputuser < 5
print ("kurang dari 5 = ",kurangdari)

# --------0+++++++++5-----------
# memeriksa angka diantara 0 sampai 5
# pakai AND (&)
corect1 = lebihdari & kurangdari 
print("angka diantara 0 sampai 5 = ",corect1)

# ------------8++++++++++++
# memeriksa angka lebih dari 8
lebihdari = inputuser > 8
print("lebih dari 8 = ",lebihdari)

# +++++++++11-------------
# memeriksa angka kurang dari 11
kurangdari = inputuser < 11
print("kurang dari 11 = ",kurangdari)

# -------8++++++++++11------------
# memeriksa angka diantara 8 sampai 11
# pakai AND (&)
corect2 = lebihdari & kurangdari
print("angka diantara 8 sampai 11 = ",corect2)

# total 
# memeriksa angka diantara 0-5 atau 8-11
# pakai OR (|)
corect = corect1 | corect2
print ("maka nilai yang anda masukan adalah = ",corect)


# No.2 ++++++++0-------5++++++++8-------11+++++++++
print("========================\nNo 2. ++++++++0-------5++++++++8-------11+++++++++\n")
inputuser = float(input("Masukan angka kurang dari 0 atau\ndiantara 5 sampai 8 atau\nlebih dari 11 = "))
print ("\n===========HASIL===========\n")

# ++++++++++++0-------------
# memeriksa angka kurang dari 0
kurangdari1 = inputuser < 0
print("kurang dari 0 = ", kurangdari1)

# -------------5++++++++++++++
# memeriksa angka lebih dari 5
lebihdari = inputuser > 5
print ("lebih dari 5 = ",lebihdari)

# +++++++++++++8------------
# memeriksa angka kurang dari 8
kurangdari = inputuser < 8
print ("kurang dari 8 = ",kurangdari)

# --------5+++++++++++8----------
# memeriksa angka diantara 5 sampai 8
# pakai AND (&)
corect1 = lebihdari & kurangdari 
print("angka diantara 5 sampai 8 = ",corect1)

# ------------11++++++++++++
# memeriksa angka lebih dari 11
lebihdari1 = inputuser > 11
print("lebih dari 11 = ",lebihdari1)

# total 
# memeriksa angka kurang dari 0 atau diantara 5-8 atau lebih dari 11
# pakai OR (|)
corect = kurangdari1 | corect1 | lebihdari1
print ("maka nilai yang anda masukan adalah = ",corect)
