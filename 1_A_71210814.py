#Yoan Adhitama
#UG10_A_71210814


#input
a = float(input ("masukan nilai rata-rata UG anda : "))
b = float(input ("Masukan nilai TTS anda : "))
c = float(input ("Masukan nilai TAS anda : "))

#case
UG = float(70/100 * a) 
TTS = float(15/100 * b)
TAS = float(15/100 * c)
na = UG + TTS + TAS

print ("================================")
print ("Nilai anda : ", na )
if (na >= 85) :
    print ("Nilai huruf anda : A ")
elif (na >= 80) : 
    print ("Nilai huruf anda : A- ")
elif (na >= 75) :
    print ("Nilai huruf anda : B+ ")
elif (na >= 70) :
    print ("Nilai huruf anda : B ")
elif (na >= 65) : 
    print ("Nilai huruf anda : B- ")
elif (na >= 60) :
    print ("Nilai huruf anda : C+ ")
elif (na >= 55) :
    print ("Nilai huruf anda : C ")
elif (na >= 45) : 
    print ("Nilai huruf anda : D ")
else : 
    print ("Nilai huruf anda : E ")
    