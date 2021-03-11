print("Soal 1")
print("Membuat program perhitungan luas persegi panjang, luas lingkaran, luas kubus, konversi suhu celcius ke farenheit, dan konversi suhu reamur ke kelvin")

import math

#menampilkan informasi program
print("1. Menghitung Luas Persegi Panjang")

#input nilai panjang dan lebar
p = float(input("Masukkan nilai panjang: "))
l = float(input("Masukkan nilai lebar: "))

#menghitung luas persegi panjang
luas_persegi_panjang = p * l

#menampilkan hasil perhitungan kelayar
print("Luas Persegi Panjang: ", luas_persegi_panjang)

#menampilkan informasi program
print("2. Menghitung Luas Lingkaran")

#input nilai jari-jari
r = float(input("Masukkan nilai jari-jari: "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menampilkan hasil perhitungan kelayar
print("Luas Lingkaran: ", luas_lingkaran)

#menampilkan informasi program
print("3. Menghitung Luas Kubus")

#input nilai sisi kubus
s = float(input("Masukkan sisi kubus: "))

#menghitung luas kubus
luas_kubus = 6 * (s ** 2)

#menampilkan hasil perhitungan kelayar
print("Luas Kubus: ", luas_kubus)

#menampilkan informasi program
print("4. Menghitung Konversi Suhu Celcius ke Farenheit")

#input suhu dalam celcius
C = float(input("Masukkan suhu (celcius): "))

#melakukan konversi suhu ke farenheit
F = (C * 9 / 5) + 32

#menampilkan hasil konversi
print("Celcius: ", C)
print("Farenheit: ", F)

#menampilkan informasi program
print("5. Menghitung Konversi Suhu Reamur ke Kelvin")

#input suhu dalam reamur
R = float(input("Masukkan suhu (reamur): "))

#melakukan konversi suhu ke kelvin
K = 5 / 4 * R + 273

#menampilkan hasil konversi
print("Reamur: ", R)
print("Kelvin: ", K)



