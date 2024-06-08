# Fungsi untuk melakukan operasi perkalian
def perkalian(a, b):
    return a * b

# Fungsi untuk melakukan operasi pengurangan
def pengurangan(a, b):
    if b != 0:
        return a / b

# Fungsi untuk melakukan operasi penambahan
def penambahan(a, b):
    return a + b

# Fungsi untuk melakukan operasi pembagian
def pembagian(a, b):
    return a - b

# Fungsi untuk memilih operasi matematika
def pilih_operasi():
    print("Pilih operasi matematika:")
    print("1. Perkalian")
    print("2. pengurangan")
    print("3. penambahan")
    print("4. pembagian")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    return pilihan

# Main program
if __name__ == "__main__":
    while True:
        operasi = pilih_operasi()

        # Memasukkan dua angka sebagai input
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        # Melakukan operasi sesuai dengan pilihan pengguna
        if operasi == '1':
            print(f"Hasil perkalian dari {angka1} dan {angka2} adalah: {perkalian(angka1, angka2)}")
        elif operasi == '2':
            print(f"Hasil pengurangan dari {angka1} dan {angka2} adalah: {pengurangan(angka1, angka2)}")
        elif operasi == '3':
            print(f"Hasil penambahan dari {angka1} dan {angka2} adalah: {penambahan(angka1, angka2)}")
        elif operasi == '4':
            print(f"Hasil pembagian dari {angka1} dan {angka2} adalah: {pembagian(angka1, angka2)}")
        else:
            print("Pilihan tidak valid.")

        ulangi = input("Apakah ingin melakukan operasi lagi? (y/n): ")
        if ulangi.lower() != 'y':
            break
