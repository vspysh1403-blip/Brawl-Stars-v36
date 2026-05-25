# Файл: Database/player_profile.py

class PlayerProfile:
    def __init__(self):
        # Твои заветные бесконечные ресурсы для приватного сервера v36!
        self.gems = 999999
        self.gold = 999999
        self.star_points = 999999
        
        # Данные твоего аккаунта
        self.username = "Developer"
        self.trophies = 50000
        self.level = 120
        
        # Настройки персонажей (открываем Базза!)
        self.unlocked_brawlers = ["SHELLY", "BUZZ", "COLT", "POCO", "EL_PRIMO"]
        self.selected_brawler = "BUZZ"

    def get_profile_bytes(self):
        """Безопасная функция: пакует данные для отправки в чистый клиент"""
        return f"{self.username}_{self.gems}_{self.gold}_{self.selected_brawler}".encode('utf-8')
