# input() = mengambil inputan dari keyboard
# int() = fungsi untuk mengkonversi nilai ke integer

alpha = 0.8

s1 = int(input('Masukkan data aktual di hari ke 1 : '))
s2 = int(input('Masukkan data aktual di hari ke 2 : '))
rumus_s2 = alpha * s2 + (1 - alpha) * s1

s3 = int(input('Masukkan data aktual di hari ke 3 : '))
rumus_s3 = alpha * s3 + (1 - alpha) * rumus_s2

s4 = int(input('Masukkan data aktual di hari ke 4 : '))
rumus_s4 = alpha * s4 + (1 - alpha) * rumus_s3

s5 = int(input('Masukkan data aktual di hari ke 5 : '))
rumus_s5 = alpha * s5 + (1 - alpha) * rumus_s4

s6 = int(input('Masukkan data aktual di hari ke 6 : '))
rumus_s6 = alpha * s6 + (1 - alpha) * rumus_s5

print("Data ramalan di hari ke 7 : " + str(rumus_s6))