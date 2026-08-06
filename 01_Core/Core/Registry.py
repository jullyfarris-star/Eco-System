from typing import Dict, List
from Core.EventBus import EventBus

class Registry:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        # Карта модулів: {module_name: {"events_in": [], "events_out": []}}
        self._modules: Dict[str, Dict[str, List[str]]] = {}

    def register_module(self, module_name: str, events_in: List[str], events_out: List[str]):
        """Реєструє модуль у системі."""
        self._modules[module_name] = {
            "events_in": events_in,
            "events_out": events_out
        }

    def subscribe_module(self, module_name: str, handler_map: Dict[str, callable]):
        """Підписує модуль на події через EventBus."""
        if module_name in self._modules:
            for event_name, handler in handler_map.items():
                self.event_bus.subscribe(event_name, handler)

    def list_modules(self) -> Dict[str, Dict[str, List[str]]]:
        """Повертає карту зареєстрованих модулів."""
        return self._modules

    def list_dependencies(self) -> Dict[str, Dict[str, List[str]]]:
        """Показує, хто слухає які події та що генерує."""
        return {
            module: {
                "listens": data["events_in"],
                "generates": data["events_out"]
            }
            for module, data in self._modules.items()
        }
