import dino090

matriks_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriks_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("=== Pengujian Modul dino090 ===")

print("\n1. Hasil Penjumlahan Matriks A dan B:")
hasil_tambah = dino090.tambah_matriks(matriks_A, matriks_B)
for baris in hasil_tambah:
    print(baris)

print("\n2. Hasil Transpose Matriks A:")
hasil_transpose = dino090.transpose_matriks(matriks_A)
for baris in hasil_transpose:
    print(baris)

print("\n3. Hasil Perkalian Matriks A dan B:")
hasil_kali = dino090.kali_matriks(matriks_A, matriks_B)
for baris in hasil_kali:
    print(baris)