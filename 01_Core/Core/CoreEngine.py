import time
from Core.EventBus import EventBus
from Core.Registry import Registry

class CoreEngine:
    def __init__(self):
        self.event_bus = EventBus()
        self.registry = Registry(self.event_bus)
        self.tick_count = 0
        self.running = False

    def start(self):
        """Запускає симуляцію MotherCube."""
        self.running = True
        self.event_bus.publish("SystemStart", {"status": "running"})
        print("🚀 CoreEngine запущено.")

    def stop(self):
        """Зупиняє симуляцію."""
        self.running = False
        self.event_bus.publish("SystemStop", {"status": "stopped"})
        print("🛑 CoreEngine зупинено.")

    def tick(self):
        """Виконує один цикл симуляції."""
        if not self.running:
            print("⚠️ CoreEngine не запущено.")
            return
        self.tick_count += 1
        event_data = {"tick": self.tick_count, "timestamp": time.time()}
        self.event_bus.publish("TickEvent", event_data)
        print(f"⏱️ Tick {self.tick_count} виконано.")

    def get_status(self):
        """Повертає статус ядра."""
        return {
            "running": self.running,
            "tick_count": self.tick_count,
            "modules": self.registry.list_modules()
        }
