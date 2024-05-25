#include <iostream>
using namespace std;

int main() {
    int n, i, j, s;

    cout << "Masukan jumlah baris : ";
    cin >> n;

    for (i = 1; i <= n; i++) { // Loop untuk setiap baris
        for (s = i; s < n; s++) // Loop untuk spasi
            cout << " ";
        for (j = 1; j <= i; j++) // Loop untuk bintang
            cout << "*";
        cout << "\n";
    }

    return 0;
}