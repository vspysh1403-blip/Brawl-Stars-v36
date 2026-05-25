# Файл: Logic/maps.py

class TrophyThievesMaps:
    def __init__(self):
        # Наш архив из 6 пляжных карт для режима «Похитители трофеев»
        self.maps = {
            101: {"name": "В лабиринте", "type": "Пляж", "safe_zone": True},
            102: {"name": "Контрабандисты", "type": "Пляж", "safe_zone": True},
            103: {"name": "Открытый берег", "type": "Пляж", "safe_zone": False},
            104: {"name": "Морские волки", "type": "Пляж", "safe_zone": True},
            105: {"name": "Песчаный тупик", "type": "Пляж", "safe_zone": False},
            106: {"name": "Аквапарк Базза", "type": "Пляж", "safe_zone": True}
        }

    def get_map_info(self, map_id):
        """Безопасная функция: выдает данные карты в игру"""
        return self.maps.get(map_id, {"name": "Стандартная карта", "type": "Пляж", "safe_zone": True})
