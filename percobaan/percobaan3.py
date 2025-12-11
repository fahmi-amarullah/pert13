try:
    val = int(input("Masukkan sebuah angka bilangan positif: "))
    print("Anda memasukkan:", val)
    hasil = 10 / val
    print("10 dibagi angka tersebut adalah:", hasil)
except ValueError:
    print("Input salah, pastikan Anda memasukkan angka, bukan huruf.")
except ZeroDivisionError:
    print("Input salah, angka tidak boleh nol.")
except Exception as e:
    print(f"Terjadi error yang tidak diketahui: {e}")
