#menampilkan luas lingkaran
print("menghitung luas lingkaran")
# input nilai
r = float(input("Masukkan nilai jari-jari: "))
# menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)
# menampilan hasil perhitungan kelayar
print("luas_lingkaran adalah: ", (luas_lingkaran))

#menampilkan luas kubus
print("menghiung luas kubus")
#input nilai
s = float(input("masukkan nilai sisi: "))
#menghitung luas kubus
luas_kubus = 6 * s**2
#menampilkan hasil perhitungan ke layar
print("luas_kubus adalah: ", (luas_kubus))

#menampilkan luas persegi panjang
print("menghitung luas persegi panajng")
#input nilai
panjang = float(input("masukkan nilai panjang: "))
lebar = float(input("masukkan nilai lebat: "))
#menghitung luas persegi panjang
luas_persegipanjang = panjang * lebar
#menampilkan hasil perhitungan ke layar
print("luas_persegipanjang adalah: ", (luas_persegipanjang))

#menampilkan informasi pengkonversi suhu celcius ke fahrenheit
print("konversi suhu celcius ke fahrenheit")
#input nilai
C = float(input("masukkan nilai suhu dalam celcius: "))
#menghitung hasil pengkonversian
C_F = 9 * (C + 32) / 5
#menampilkan hasil hitung pengkonversian
print("Besar suhu dalam fahrenheit adalah: ", C_F)

#menampilkan informasi pengkonversian suhu reamur ke kelvin
print("konversi suhu reamur ke kelvin")
#input nilai
R = float(input("masukkan nilai suhu dalam reamur: "))
#menghitung hasil pengkonversian
R_K = 5 * (R + 273) / 4
#menampilkan  hasil hitung pengkonversian
print("konversi suhu dalam kelvin: ", R_K)