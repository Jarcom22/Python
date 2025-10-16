import socket
import threading

# Menyimpan daftar client yang terhubung
clients = []

# Fungsi untuk mengirim pesan ke semua client (broadcast)
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Fungsi untuk menangani client
def handle_client(conn, addr):
    print(f"[TERHUBUNG] {addr} bergabung ke server.")
    conn.send("Selamat datang di Chat Room!\n".encode('utf-8'))
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            print(f"[{addr}] {message.decode('utf-8')}")
            broadcast(message, conn)
        except:
            # Jika client terputus atau error
            print(f"[PUTUS] {addr} terputus.")
            conn.close()
            clients.remove(conn)
            break

# Fungsi utama server
def start_server():
    host = '127.0.0.1'  # alamat lokal
    port = 55555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[MENUNGGU KONEKSI] Server berjalan di {host}:{port}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
