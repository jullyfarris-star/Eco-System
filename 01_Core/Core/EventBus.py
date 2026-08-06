from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        # Словник подій: {event_name: [список слухачів]}
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, handler: Callable):
        """Підписати модуль на подію."""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: Callable):
        """Відписати модуль від події."""
        if event_name in self._subscribers:
            self._subscribers[event_name] = [
                h for h in self._subscribers[event_name] if h != handler
            ]

    def publish(self, event_name: str, data: Any = None):
        """Опублікувати подію для всіх слухачів."""
        if event_name in self._subscribers:
            for handler in list(self._subscribers[event_name]):
                handler(data)

    def list_subscribers(self) -> Dict[str, List[str]]:
        """Повертає карту підписок (для Registry)."""
        return {
            event: [h.__name__ for h in handlers]
            for event, handlers in self._subscribers.items()
        }
