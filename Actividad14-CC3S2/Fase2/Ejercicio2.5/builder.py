# builder.py
import json
from typing import Dict
from Actividad14_CC3S2.Fase2.Ejercicio2.4.composite import CompositeModule
from Actividad14_CC3S2.Fase2.Ejercicio2.2.factory import NullResourceFactory
from Actividad14_CC3S2.Fase2.Ejercicio2.3.prototype import ResourcePrototype

# Si prefieres usar imports relativos ajusta el path según donde subas los módulos

class InfrastructureBuilder:
    def __init__(self):
        self.module = CompositeModule()

    def build_null_fleet(self, count: int):
        base = NullResourceFactory.create("app")
        proto = ResourcePrototype(base)
        for i in range(count):
            def mutator(block, index=i):
                # Renombrar recurso "app" a "app_<i>"
                res = block["resource"]["null_resource"].pop("app")
                block["resource"]["null_resource"][f"app_{index}"] = res
            self.module.add(proto.clone(mutator))
        return self

    def build_group(self, name: str, size: int):
        base = NullResourceFactory.create(name)
        proto = ResourcePrototype(base)
        group = CompositeModule()
        for i in range(size):
            def mut(block, index=i):
                res = block["resource"]["null_resource"].pop(name)
                block["resource"]["null_resource"][f"{name}_{index}"] = res
            group.add(proto.clone(mut))
        # Añadimos como submodule con el formato {module: {name: <exported content>}}
        self.module.add({"module": {name: group.export()}})
        return self

    def export(self, path: str = "terraform/main.tf.json"):
        with open(path, "w") as f:
            json.dump(self.module.export(), f, indent=2)
        return path

# Si se ejecuta directamente, genera un ejemplo:
if __name__ == "__main__":
    b = InfrastructureBuilder()
    b.build_null_fleet(3)
    b.build_group("network", 2)
    out = b.export("Actividad14-CC3S2/terraform_main_example.tf.json")
    print(f"Generated {out}")