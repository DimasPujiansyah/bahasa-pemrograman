#include <iostream>

int main() {
    int angka_pertama, angka_kedua;

    std::cout << "Masukkan Angka Pertama: ";
    std::cin >> angka_pertama;

    std::cout << "Masukkan Angka Kedua: ";
    std::cin >> angka_kedua;

    int penjumlahan = angka_pertama + angka_kedua;
    int pengurangan = angka_pertama - angka_kedua;
    int perkalian = angka_pertama * angka_kedua;
    int pembagian = angka_pertama / angka_kedua;

    std::cout << "Penjumlahan : " << penjumlahan << std::endl;
    std::cout << "Pengurangan : " << pengurangan << std::endl;
    std::cout << "Perkalian: " << perkalian << std::endl;
    std::cout << "Pembagian: " << pembagian << std::endl;

    return 0;
}