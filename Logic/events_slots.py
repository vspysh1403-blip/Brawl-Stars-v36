# Файл: Logic/events_slots.py

class EventSlots:
    def __init__(self):
        # Настраиваем активный слот события для чистого клиента игры
        self.slot_id = 1
        self.game_mode = "TrophyThieves"
        self.active_map_id = 101  # Начнем с первой пляжной карты "В лабиринте"

    def get_current_event(self):
        """Передает клиенту информацию о текущем режиме и карте"""
        return {
            "slot": self.slot_id,
            "mode": self.game_mode,
            "map_id": self.active_map_id
        }
