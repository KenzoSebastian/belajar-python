# operasi yang dapat di dilakukan dengan menyingkatan 
# operator ditambah dengan assignment

a = 5 # adalah assigment
print("nilai a =",a)

# operasi aritmatika
print("\n============OPERASI ARITMATIKA=============")
a += 1 #artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi :",a)

a -= 2 #artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi :",a)

a *= 5 #artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi :",a)

a /= 2 #artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi :",a)

# modulus dan floor division
print("\n============MODULUS DAN FLOOR DIVISION=============")
b = 10
print("nilai b =",b)
b %= 3 #artinya adalah b = b % 3
print("nilai a %= 3, nilai b menjadi :",b)

b = 10
print("\nnilai b =",b)
b //= 3 #artinya adalah b = b // 3 
print("nilai a //= 3, nilai b menjadi :",b)

# pangkat atau eksponen
print("\n============PANGKAT ATAU EKSPONEN=============")
a = 5
print("nilai a =",a)
a **= 3 #artinya adalah a = a ** 3 
print("nilai a **= 3, nilai a menjadi :",a)

# operasi bitwise
# OR
print("\n============OR=============")
c = True
print("nilai c =",c)
c |= False #artinya adalah c = c | False 
print("nilai c |= False, nilai c menjadi :",c)

c = False
print("\nnilai c =",c)
c |= False #artinya adalah c = c | False 
print("nilai c |= False, nilai c menjadi :",c)

# AND
print("\n============AND=============")
c = True
print("nilai c =",c)
c &= False #artinya adalah c = c & False 
print("nilai c &= False, nilai c menjadi :",c)

c = True
print("\nnilai c =",c)
c &= True #artinya adalah c = c & False 
print("nilai c &= True, nilai c menjadi :",c)

# XOR
print("\n============XOR=============")
c = True
print("nilai c =",c)
c ^= False #artinya adalah c = c ^ False 
print("nilai c ^= False, nilai c menjadi :",c)

c = True
print("\nnilai c =",c)
c ^= True #artinya adalah c = c ^ False 
print("nilai c ^= True, nilai c menjadi :",c)

# geser geser
print("\n============GESER GESER=============")
d = 0b0100
print("nilai d =",format(d,'04b'))
d >>= 2 #artinya adalah d = d >> 2 
print("nilai d >>= 2, nilai d menjadi :",format(d,'04b'))
d <<= 1 #artinya adalah d = d << 1 
print("nilai d <<= 1, nilai d menjadi :",format(d,'04b'))






