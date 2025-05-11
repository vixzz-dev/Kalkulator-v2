from decimal import Decimal, getcontext

# Set precision tinggi, bisa diubah sesuai kebutuhan
getcontext().prec = 100

def kalkulator():
    print("=== Kalkulator Dasar (Presisi Tinggi) ===")
    print("Operasi yang tersedia: +  -  *  /")
    
    while True:
        try:
            angka1 = Decimal(input("Masukkan angka pertama: "))
            operator = input("Masukkan operator (+, -, *, /): ")
            angka2 = Decimal(input("Masukkan angka kedua: "))

            if operator == '+':
                hasil = angka1 + angka2
            elif operator == '-':
                hasil = angka1 - angka2
            elif operator == '*':
                hasil = angka1 * angka2
            elif operator == '/':
                if angka2 == 0:
                    print("Error: Pembagian dengan nol tidak diperbolehkan.")
                    continue
                hasil = angka1 / angka2
            else:
                print("Operator tidak dikenali.")
                continue

            print(f"Hasil: {hasil}\n")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

        lanjut = input("Hitung lagi? (y/n): ")
        if lanjut.lower() != 'y':
            print("Terima kasih telah menggunakan kalkulator.")
            break

# Jalankan kalkulator
kalkulator()
