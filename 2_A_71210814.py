#Yoan Adhitama
#UG10_A_71210814

#Menu
print ("1. Menghitung sisa hasil bagi")
print ("2. Membulatkan ke bawah hasil pembagian")
print ("3. Mencari akar kubik sebuah bilangan")

a = float(input("Masukan menu yang anda pilih : "))

#Case
if a == 1 :
    b = float(input("Masukan bilangan yang ingin dibagi : "))
    c = float(input("Masukan bilangan pembagi : "))
    d = b % c
    print ("Sisa hasil bagi", b , "dibagi dengan", c , "adalah", d)
elif a == 2 : 
    b = float(input("Masukan bilangan yang ingin dibagi : "))
    c = float(input("Masukan bilangan pembagi : "))
    d = b % c 
    print ("Hasil pembagian", b , "dibagi dengan", c , "dibulatkan kebawah adalah", b//c )
elif a == 3 : 
    e = float(input("Masukan bilangan yang ingin dicari akar kubiknya : "))
    f = 1/3 
    print ("Akar kubik dari", e , "adalah" , e**f)

