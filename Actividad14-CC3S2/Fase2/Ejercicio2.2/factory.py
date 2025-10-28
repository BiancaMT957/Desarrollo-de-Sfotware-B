
# factory.py
import uuid
from datetime import datetime
from typing import Dict, Optional

class NullResourceFactory:
    @staticmethod
    def create(name: str, triggers: Optional[Dict] = None) -> Dict:
        triggers = triggers or {
            "factory_uuid": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat()
        }
        return {
            "resource": {
                "null_resource": {
                    name: {"triggers": triggers}
                }
            }
        }

class TimestampedNullResourceFactory(NullResourceFactory):
    @staticmethod
    def create(name: str, fmt: str, extra: Optional[Dict] = None) -> Dict:
        """
        Crea triggers con timestamp formateado según fmt.
        fmt es un string aceptado por datetime.strftime, por ejemplo '%Y%m%d'.
        """
        ts = datetime.utcnow().strftime(fmt)
        triggers = {"timestamp_formatted": ts}
        if extra:
            triggers.update(extra)
        # Heredamos el resto del comportamiento
        return {
            "resource": {
                "null_resource": {
                    name: {"triggers": triggers}
                }
            }
        }