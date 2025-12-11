try:
    x = int(input("masukan angka:"))
except ValueError:
    print("itu bukan angka")
else:
    print(f"terimakasih, anda memasukan angka {x}")
finally:
    print("sesi input selesai (blok finally selalu dieksekusi).")

    