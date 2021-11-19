#Yoan Adhitama
#UG10_A_71210814

#input
a = input("Masukkan artikel yang ingin dipindai : ")
b = input("Masukkan nama klub favorit anda : ")
c = input("Masukkan score yang ingin dicari : ")

#case
if ((c and b) in a) :
    print("Hasil pencarian ditemukan")
elif c in a:
    print("Hanya skor {} yang ditemukan pada artikel ini".format(c))
elif b in a:
    print("Hanya kata {} yang ditemukan pada artikel ini".format(b))
else:
    print("Hasil pencarian {} dan {} tidak ditemukan".format(b,c))
