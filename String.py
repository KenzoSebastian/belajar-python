data = "ini adalah string"
print(data)
print(type(data))

#1. cara membuat string

'''
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = 'menggunakan double quote'
print(data)

print('"Halo apa kabar"')
print("'Halo apa kabar'")
print("ini adalah hari jum'at")

#2. mengunakan tanda \

# membuat tanda ' menjadi string
print(r"========(\)=======")
print('hari jum\'at kita main')
print('g\'day, isn\'t it?')

# backslash (agar \ bisa berfungsi sebagai \ , kita harus mendouble \ menjadi \\)
print(r"========(\\)=======")
print("C:\\user\\desktop\\kenzo\\CODING")

# tab (\t)
print(r"========(\t)=======")
print("Kenzo\tTessa, menjauh")
print("Kenzo\t\tTessa, lebih jauh")
print("Kenzo\t\t\tTessa, semakin jauh")

# backspace (\b)
print(r"========(\b)=======")
print("Kenzo \bTessa, kehapus spasi")
print("Kenzo \b\bTessa, kehapus o")
print("Kenzo \b\b\bTessa, kehapus o dan z")

# newline (\n) (\r)
print(r"========(\n)(\r)=======")
print("baris pertama,\nbaris kedua") # LF -> line feed -> unix, macos
print("baris pertama,\rbaris kedua") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama,\r\nbaris kedua") # CRLF -> line feed carriage return -> window

#3. string literal dan raw

# hati hati
print("C:\new folder") # akan salah path nya

# menggunakan raw string (semua di dalam raw akan menjadi string)
print(r"========RAW=======")
print(r"C:\new folder")
print(r'aku adalah\tanak\nyang\baik')

# multiline literal string
print(r"========multiline literal string=======")
print("""
Nama : Kenzo
Kelas : 17.1c
""")

# multiline literal string dan raw
print(r"========multiline literal string + raw=======")
print(r"""
Nama : Kenzo sebastian
Kelas : 17.1c\new normal
""")

