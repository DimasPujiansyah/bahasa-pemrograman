#include <iostream>
using namespace std;

// Fungsi Perkalian
double perkalian(double a, double b) {
    return a * b;
}

// Fungsi Pembagian
double pembagian(double a, double b) {
    if (b == 0) {
        cout << "Error: Pembagian dengan nol" << endl;
        return 0;
    } else {
        return a / b;
    }
}

// Fungsi Penjumlahan
double penjumlahan(double a, double b) {
    return a + b;
}

// Fungsi Pengurangan
double pengurangan(double a, double b) {
    return a - b;
}

// Menu Program
void mainMenu() {
    cout << "Pilih Menu Aritmetika Dasar:" << endl;
    cout << "1. Perkalian" << endl;
    cout << "2. Pembagian" << endl;
    cout << "3. Penjumlahan" << endl;
    cout << "4. Pengurangan" << endl;
    cout << "5. Keluar!!" << endl;
}

int main() {
    int pilihan;
    double angka1, angka2;

    while (true) {
        mainMenu();
        cout << "Pilih Menu (1/2/3/4/5): ";
        cin >> pilihan;

        if (pilihan == 5) {
            cout << "Terima kasih!" << endl;
            break;
        }

        if (pilihan >= 1 && pilihan <= 4) {
            cout << "Masukkan angka pertama: ";
            cin >> angka1;
            cout << "Masukkan angka kedua: ";
            cin >> angka2;

            switch (pilihan) {
                case 1:
                    cout << "Hasil perkalian: " << perkalian(angka1, angka2) << endl;
                    break;
                case 2:
                    cout << "Hasil pembagian: " << pembagian(angka1, angka2) << endl;
                    break;
                case 3:
                    cout << "Hasil penjumlahan: " << penjumlahan(angka1, angka2) << endl;
                    break;
                case 4:
                    cout << "Hasil pengurangan: " << pengurangan(angka1, angka2) << endl;
                    break;
            }
        } else {
            cout << "Pilihan tidak valid!" << endl;
        }
    }

    return 0;
}
