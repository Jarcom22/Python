import socket
import threading

# Fungsi untuk menerima pesan dari server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("⚠️ Koneksi terputus dari server.")
            client.close()
            break

# Fungsi untuk mengirim pesan ke server
def send_messages(client):
    while True:
        try:
            message = input("")
            client.send(message.encode('utf-8'))
        except:
            print("⚠️ Gagal mengirim pesan.")
            client.close()
            break

# Fungsi utama client
def start_client():
    host = '127.0.0.1'  # harus sama dengan alamat server
    port = 55555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except:
        print("❌ Tidak dapat terhubung ke server.")
        return

    print("✅ Terhubung ke server. Anda dapat mulai mengirim pesan.")

    # Jalankan dua thread: satu untuk menerima, satu untuk mengirim
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
