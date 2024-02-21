# sebelum pake format
nama = "Kenzo"
angka = 18
boolean = True
format_biasa = "hai nama saya " + nama + " saya berumur " + str(angka) + ", apakah saya manusia ? : " + str(boolean) # lebih panjang dan hrs di casting
print("Sebelum Pakai Format".center(35, "="))
print(format_biasa)

# sebelum pake format
nama = "Kenzo"
angka = 18
boolean = True
format_biasa = f"hai nama saya {nama} sayaa berumur {angka}, apakah saya manusia ? : {boolean}" # lebih pendek dan praktis
print("Sesudah Pakai Format".center(35, "="))
print(format_biasa)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilakan tanda + dan -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
persen = 0.045
format_persen = f"persen = {persen:.1%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain(binary, octal, hexadecimal)

angka = 5099
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex) 