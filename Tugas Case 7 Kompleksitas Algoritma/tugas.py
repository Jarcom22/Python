# Program: Kombinasi Koin dengan Algoritma Greedy

# Input jumlah uang
amount = int(input("Masukkan jumlah uang: "))

# Input daftar nilai koin (misal: 1000 500 200 100 50)
coins = list(map(int, input("Masukkan nilai koin (pisahkan dengan spasi): ").split()))

# Urutkan koin dari besar ke kecil
coins.sort(reverse=True)

print("\nKombinasi koin yang digunakan:")

remaining = amount
coin_count = 0

# Proses algoritma Greedy
for coin in coins:
    count = remaining // coin  # Berapa kali koin ini bisa digunakan
    if count > 0:
        print(f"{coin} x {count}")
        coin_count += count
        remaining -= coin * count

# Hasil akhir
print(f"\nJumlah total koin: {coin_count}")
if remaining > 0:
    print(f"Sisa uang yang tidak bisa ditukar: {remaining}")
