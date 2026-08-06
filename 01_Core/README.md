01_Core
=======
Коротко:
- Папка з базовими ядровими модулями проєкту (Core).
- Містить клас EventBus для підписки/публікації подій та інші базові компоненти.

Поточні файли:
- Core/EventBus.py — реалізація EventBus (публікація/підписка подій).
- Core/Registry.py — реєстр модулів для збереження інформації про вхідні/вихідні події.

Як використовувати:
1. Імпортуйте модулі:
   from Core.EventBus import EventBus
   from Core.Registry import Registry
2. Створіть екземпляри та реєструйте модулі:
   bus = EventBus()
   registry = Registry(bus)
   registry.register_module("PhysicsEngine", ["TICK_EVENT"], ["PHYSICS_UPDATE"]) 

Ліцензія:
- Проєкт має LICENSE у корені — дотримуйтеся цієї ліцензії.
