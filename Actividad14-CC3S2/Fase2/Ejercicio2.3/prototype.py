
# prototype.py
from copy import deepcopy
from typing import Callable, Dict

class ResourcePrototype:
    def __init__(self, template: Dict):
        self.template = template

    def clone(self, mutator: Callable[[Dict], None]) -> Dict:
        new_copy = deepcopy(self.template)
        # Mutator modifica la copia in-place
        mutator(new_copy)
        return new_copy

# Ejemplo de mutator avanzado que añade un local_file
def add_welcome_file(block: Dict):
    # Asume que nombramos el recurso previamente como app_0
    # Añadimos trigger y local_file
    nr = block.get("resource", {}).get("null_resource", {})
    if nr:
        key = next(iter(nr.keys()))
        nr[key]["triggers"]["welcome"] = "¡Hola!"
    # Añadir local_file al bloque
    block.setdefault("resource", {})
    block["resource"]["local_file"] = {
        "welcome_txt": {
            "content": "Bienvenido",
            "filename": "${path.module}/bienvenida.txt"
        }
    }