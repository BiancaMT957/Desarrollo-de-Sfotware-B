# singleton.py
import threading
from datetime import datetime
from typing import Dict

class SingletonMeta(type):
    _instances: Dict[type, object] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigSingleton(metaclass=SingletonMeta):
    def __init__(self, env_name: str):
        self.env_name = env_name
        self.settings: dict = {}
        self.created_at: str = datetime.utcnow().isoformat()

    def reset(self):
        """
        Limpia settings pero mantiene created_at y env_name.
        """
        # Mantener created_at y env_name intactos
        self.settings.clear()
        # No re-asignamos created_at
        return self