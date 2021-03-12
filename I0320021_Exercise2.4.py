#menampilkan informasi programe

print("Konversi suhu (Fahrenheit ke Celcius)")

#input suhu dalam fahrenheit
F = float(input("Masukkan suhu(fahrenheit): "))

#melakukan konversi suhu fahrenheit ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahrenheit: ", F)
print("Celcius: ", C)