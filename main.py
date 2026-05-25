import socket
import threading
import sys
from Protocol.crypto import BrawlCrypto
from Logic.events_slots import EventSlots
from Logic.maps import TrophyThievesMaps

class BrawlServer:
    def __init__(self, host='0.0.0.0', port=9339):
        self.host = host
        self.port = port
        self.crypto = BrawlCrypto()
        self.slots = EventSlots()
        self.maps = TrophyThievesMaps()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server.bind((self.host, self.port))
        except Exception as e:
            print(f"[Ошибка] Не удалось запустить сервер: {e}")
            sys.exit()
            
        server.listen(5)
        print("--------------------------------------------------")
        print("[СЕРВЕР v36] Твой приватный сервер успешно запущен!")
        print("[СЕРВЕР v36] Ожидание подключения чистого клиента Brawl Stars...")
        print("--------------------------------------------------")

        while True:
            client_socket, address = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket, address)).start()

    def handle_client(self, client, addr):
        print(f"[Подключение] Игрок вошел в игру с адреса: {addr}")
        try:
            while True:
                header = client.recv(7)
                if not header or len(header) < 7:
                    break
                
                packet_id = int.from_bytes(header[0:2], byteorder='big')
                packet_len = int.from_bytes(header[2:5], byteorder='big')
                encrypted_data = client.recv(packet_len)
                
                decrypted_data = self.crypto.decrypt_packet(packet_id, encrypted_data)
                print(f"[Пакет] Получен ID {packet_id}, длина {packet_len} байт. Обработка...")
                
                if packet_id == 10101:
                    login_ok = int(20104).to_bytes(2, 'big') + int(0).to_bytes(3, 'big') + int(0).to_bytes(2, 'big')
                    client.send(login_ok)
                    print("[Сервер] Пакет LoginOk отправлен. Игрок в главном меню!")
                    
        except ConnectionResetError:
            print(f"[Связь] Игрок {addr} закрыл игру.")
        finally:
            client.close()

if __name__ == "__main__":
    server = BrawlServer()
    server.start()
