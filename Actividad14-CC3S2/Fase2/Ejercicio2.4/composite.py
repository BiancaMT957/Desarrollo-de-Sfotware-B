# composite.py
from typing import List, Dict

class CompositeModule:
    def __init__(self):
        self.children: List[Dict] = []

    def add(self, block: Dict):
        """
        block puede contener keys 'resource' y/o 'module'.
        """
        self.children.append(block)

    def export(self) -> Dict:
        merged: Dict = {"resource": {}, "module": {}}
        for child in self.children:
            # Merge modules
            if "module" in child:
                for mname, mcontent in child["module"].items():
                    # Simple merge: si existe, update (no detección de colisiones)
                    if mname in merged["module"]:
                        # fusionar resources y module internos si aplica
                        for k, v in mcontent.items():
                            if isinstance(v, dict):
                                merged["module"][mname].setdefault(k, {}).update(v)
                            else:
                                merged["module"][mname][k] = v
                    else:
                        merged["module"][mname] = mcontent
            # Merge resources
            if "resource" in child:
                for rtype, ressources in child["resource"].items():
                    merged["resource"].setdefault(rtype, {}).update(ressources)
        # Limpieza: si no hay módulos, eliminar la key para compatibilidad con terraform
        if not merged["module"]:
            merged.pop("module")
        return merged