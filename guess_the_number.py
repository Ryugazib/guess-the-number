import random

angka = random.randint (1, 10)
sapaan_awal = ('HAI SELAMAT DATANG DI GAME TEBAK ANGKA')

print ('********************************************')
print (f'** {sapaan_awal} **')
print ('********************************************')

nama_user = input ('MASUKKAN NAMA: ')
print (f'HAI {nama_user} SELAMAT DATANG')

percobaan = 3
tebakan_angka = int(input ('SILAHKAN TEBAK ANGKA 1-10: '))

while percobaan > 0 and tebakan_angka != angka: 
    percobaan -= 1

    if tebakan_angka < angka:
        print(f'MAAF ANDA SALAH ANGKA TERSEBUH LEBIH TINGGI [ANDA MASIH PUNYA {percobaan} PERCOBAAN LAGI] ')
    elif tebakan_angka > angka:
        print (f'MAAF ANDA SALAH ANGKA TERSEBUT LEBIH RENDAH [ANDA MASIH PUNYA {percobaan} PERCOBAAN LAGI] ')
 
    if percobaan > 0:
        tebakan_angka = int(input ('SILAHKAN TEBAK ANGKA 1-10: '))

if tebakan_angka == angka:
    print (f'SELAMAT ANDA BENAR ANGKANYA ADALAH {angka} DAN KAMU MENJAWAB {tebakan_angka}')
else:
    print (f'MAAF ANDA KALAH ANGKANYA ADALAH {angka} DAN KAMU MENEBAK {tebakan_angka}')
