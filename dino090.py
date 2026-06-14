# File: dino090.py
# Modul Aljabar Matriks 

def tambah_matriks(matriks1, matriks2):
    """Fungsi untuk menjumlahkan dua matriks dengan ordo yang sama."""
    # Mengecek apakah ordo matriks sama
    if len(matriks1) != len(matriks2) or len(matriks1[0]) != len(matriks2[0]):
        return "Error: Ordo matriks tidak sama!"

    hasil = []
    for i in range(len(matriks1)):
        baris = []
        for j in range(len(matriks1[0])):
            # Menjumlahkan elemen pada posisi yang sama
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
    return hasil

def transpose_matriks(matriks):
    """Fungsi untuk melakukan transpose pada matriks (mengubah baris menjadi kolom)."""
    hasil = []
    for i in range(len(matriks[0])):
        baris = []
        for j in range(len(matriks)):
            baris.append(matriks[j][i])
        hasil.append(baris)
    return hasil

def kali_matriks(matriks1, matriks2):
    """Fungsi untuk mengalikan dua matriks."""
    # Mengecek syarat perkalian matriks
    if len(matriks1[0]) != len(matriks2):
        return "Error: Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua!"

    hasil = []
    for i in range(len(matriks1)):
        baris = []
        for j in range(len(matriks2[0])):
            total = 0
            for k in range(len(matriks2)):
                total += matriks1[i][k] * matriks2[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil


