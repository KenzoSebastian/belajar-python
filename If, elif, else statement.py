# If dan Else statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("Siapa nama anda? ")

# Rumus if
# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# # 1. program if inline
# if nama =="ucup": print("kamu gantenggg!!!!")
# print(f"Terima kasih {nama}")

# # 2. program if indentation
# if nama =="ucup": 
#     print("kamu gantenggg!!!!")
#     print("kamu juga kerenn!!")
# print(f"Terima kasih {nama}")

# # # 3. Else statement
# if nama=="otong":
#     print("hai otooongg, si keren")
# else:
#     print("ah kamu bukan otong")

# -------------------------------------------------------------------------
# Elif = Else If statement

if nama == "ucup": # kondisi 1
    print("hai ucup") # aksi true 1
elif nama =="otong":  # kondisi 2
    print("hai otong") # aksi true 2
elif nama =="mario": # kondisi 3
    print("hai mario") # aksi true 3
else:
    print("ah gatau ga kenal") # aksi false

print("End") 
