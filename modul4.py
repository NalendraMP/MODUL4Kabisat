print("Selamat datang di perhitungan yang menentukan jumlah hari dalam bulan")
print("------------------------------------------------------")

bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun (misalnya 2023): "))


while bulan < 1 or bulan > 12:
    print("Bulan harus dalam rentang 1-12.")
    bulan = int(input("Masukkan bulan (1-12): "))

if bulan == 2:

    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        jumlah_hari = 29
    else:
        jumlah_hari = 28
elif bulan in [4, 6, 9, 11]:
   
    jumlah_hari = 30
else:
    jumlah_hari = 31
    
print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")

print("Terimakasih sudah melihat kode saya")