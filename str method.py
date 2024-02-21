# operasi dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

print("\n" + "="*10 + "upper()" + "="*10)
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
print("\n" + "="*10 + "lower()" + "="*10)
alay = "aKu KeCe AbieezzZZzzzZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
print("\n" + "="*10 + "islower()" + "="*10)
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))

# contoh pengecekan upper case
print("\n" + "="*10 + "isupper()" + "="*10)
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() --> untuk mengecek semuanya huruf 

print("\n" + "="*10 + "isalpha()" + "="*10)
huruf = "abcde"
huruf2 = huruf.isalpha() # hasilnya bool
print(huruf + " is huruf = " + str(huruf2))

# isalnum() --> huruf dan angka

print("\n" + "="*10 + "isalnum()" + "="*10)
hurufangka = "Kenzo123"
hurufangka2 = hurufangka.isalnum() # hasilnya bool
print(hurufangka + " is huruf dan angka = " + str(hurufangka2))

# isspace() --> spasi, tab newline \n

print("\n" + "="*10 + "isspace()" + "="*10)
huruf = "\tabcde\bdfgh"
huruf2 = huruf.isspace() # hasilnya bool
print(huruf + " is spasi = " + str(huruf2))

# istitle() --> semua kata dimulai dengan huruf besar

print("\n" + "="*10 + "istitle()" + "="*10)
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() 
print("\n" + "="*10 + "startswith()" + "="*10)
cek_start = "Kenzo Sebastian".startswith("Kenzo")
print("start = " + str(cek_start))

print("\n" + "="*10 + "endswith()" + "="*10)
cek_end = "Kenzo Sebastian".endswith("Sebastian")
print("end = " + str(cek_end))

## penggabungan komponen join(), split()
print("\n" + "="*10 + "join()" + "="*10)
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan =' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan) 

print("\n" + "="*10 + "split()" + "="*10)
gabungan ="kamujadiakujadidiajadikamijadimereka"
print(gabungan.split('jadi'))


## alokasi karakter rjust(), ljust(), center()

print("\n" + "="*10 + "rjust()" + "="*10)
kanan = "kanan".rjust(30,"=")
print("|" + kanan + "|")

print("\n" + "="*10 + "ljust()" + "="*10)
kiri = "kiri".ljust(30, "-")
print("|" + kiri + "|")

print("\n" + "="*10 + "center()" + "="*10)
tengah = "tengah".center(30, "~")
print("|" + tengah + "|")

# kebalikannya -> strip()
print("\n" + "="*10 + "strip()" + "="*10)
kanan = kanan.strip("=") # menghilangkan tanda =
print("|" + kanan + "|")

print("\n" + "="*10 + "strip()" + "="*10)
kiri = kiri.strip("-") # menghilangkan tanda -
print("|" + kiri + "|")

print("\n" + "="*10 + "strip()" + "="*10)
tengah = tengah.strip("~") # menghilangkan tanda ~
print("|" + tengah + "|")

## capitalize -> untuk kapital huruf pertama
text = "kenzo sebastian"
text = text.capitalize()
print(text)

## casefold() -> untuk mengecilkan(unKapital) huruf di depan kata
text = "Hello, And Welcome To My World"
text = text.casefold()
print(text)
