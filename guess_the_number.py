import random

angka = random.randint (1, 10)
sapaan_awal = ('HAI SELAMAT DATANG DI GAME TEBAK ANGKA')

print ('********************************************')
print (f'** {sapaan_awal} **')
print ('********************************************')

nama_user = input ('MASUKKAN NAMA: ')
print (f'HAI {nama_user} SELAMAT DATANG')

tebakan_angka = int(input ('SILAHKAN TEBAK ANGKA 1-10: '))
while tebakan_angka != angka:
    print ('MAAF ANDA SALAH TEBAK SILAHKAN TEBAK LAGI: ')
    tebakan_angka = int(input ('SILAHKAN TEBAK LAGI: '))

print (f'SELAMAT KAMU BENAR ANGKANYA {angka} DAN TEBAKANMU {tebakan_angka}')