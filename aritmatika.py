#  operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi perkalian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division (hasil pembagian di bulatkan ke bawah) //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence
# urutan prioritas: tanda kurung --> exponen --> kali/bagi --> tambah/kurang

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# kurung mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)




