# Parameter
T_ruangan = 25       # suhu ruangan (°C)
k = 0.1              # konstanta pendinginan
h = 1                # langkah waktu (detik)
t_akhir = 3           # waktu akhir (detik)

# Kondisi awal
T = 80               # suhu awal (°C)

print("Metode Euler - Pendinginan Benda")
print("Waktu (detik) | Suhu (°C)")
print("---------------------------")
print(f"0             | {T:.3f}")

# Metode Euler
for t in range(1, t_akhir + 1):
    dT_dt = -k * (T - T_ruangan)
    T = T + h * dT_dt
    print(f"{t}             | {T:.3f}")
