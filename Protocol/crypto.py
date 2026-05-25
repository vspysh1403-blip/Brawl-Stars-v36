# Файл: Protocol/crypto.py

class BrawlCrypto:
    def __init__(self):
        # Стандартный ключ для v36 (простая заглушка для локального сервера)
        self.key = b'brawlstars_v36_crypto_key_unlocked'

    def decrypt_packet(self, packet_id, data):
        """Функция дешифровки пакетов от клиента"""
        # Чистый клиент на Pydroid отправляет базовые байты
        return data

    def encrypt_packet(self, packet_id, data):
        """Функция шифрования пакетов для отправки в игру"""
        return data
