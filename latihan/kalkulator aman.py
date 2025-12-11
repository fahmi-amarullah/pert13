try:
 #input angka
 a = float(input("masukan angka pertama: "))
 b = float(input("masukan angka kedua: "))

#input operator
 op = input("masukkan operator (+, -, *, /): ")

#operasi berdasarkan operator
 if op == "+":
    hasil = a + b
 elif op == "-":
    hasil = a - b
 elif op == "*":
    hasil = a * b
 elif op == "/":
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("error : pembagian dengan nol tidak diperbolehkan")
        exit()
 else:
    raise Exception("operator tidak valid gunakan hanya +, -, *, /")
 print(f"hasil : {hasil}")

except ValueError:
   print("input salah pastikan anda memasukan angka.")

except Exception as e:
   print("terjadi errpr:", e)


