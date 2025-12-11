try:
    daftar_angka = [1, 2, 3]
    indeks = int(input("masukan indeks yang ingin diakses (0-2): "))
    print("nilai:", daftar_angka[indeks])
except IndexError as e: 
    print("terjadi indexerror. pesan sistem:", e)
except ValueError as e:
    print("terjadi vallue error. pesan sistem:", e)
