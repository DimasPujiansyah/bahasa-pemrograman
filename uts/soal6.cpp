#include <iostream>
using namespace std;

// Deklarasi fungsi-fungsi
void tambah(int a, int b) {
    cout << "Hasil dari " << a << " + " << b << " = " << (a + b) << endl;
}

void kurang(int a, int b) {
    cout << "Hasil dari " << a << " - " << b << " = " << (a - b) << endl;
}

void kali(int a, int b) {
    cout << "Hasil dari " << a << " * " << b << " = " << (a * b) << endl;
}

void bagi(int a, int b) {
    if (b != 0) {
        cout << "Hasil dari " << a << " / " << b << " = " << (a / b) << endl;
    } else {
        cout << "Error: Tidak bisa membagi dengan nol." << endl;
    }
}

int main() {
    int pilih, angka1, angka2;
    cout << "SISTEM OPERASI" << endl;
    cout << "Menu" << endl;
    cout << "1. Tambah" << endl;
    cout << "2. Kurang" << endl;
    cout << "3. Kali" << endl;
    cout << "4. Bagi" << endl;
    cout << "Input (pilih): ";
    cin >> pilih;

    cout << "Input angka pertama: ";
    cin >> angka1;
    cout << "Input angka kedua: ";
    cin >> angka2;

    switch (pilih) {
        case 1:
            tambah(angka1, angka2);
            break;
        case 2:
            kurang(angka1, angka2);
            break;
        case 3:
            kali(angka1, angka2);
            break;
        case 4:
            bagi(angka1, angka2);
            break;
        default:
            cout << "Pilihan tidak ada!" << endl;
    }

    cout << "Hasil dari operasi Matematika" << endl;
    return 0;
}