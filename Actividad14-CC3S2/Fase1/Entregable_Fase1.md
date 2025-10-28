# Fase 1 — Exploración y análisis

Este documento resume los patrones aplicados en el laboratorio y responde las preguntas solicitadas.

## 1. Singleton
La metaclase `SingletonMeta` mantiene un diccionario privado `_instances` que mapea clases a sus instancias. En `__call__`, antes de crear una nueva instancia, se adquiere `_lock` (un `threading.Lock`) para evitar condiciones de carrera en entornos multihilo. Si la clase ya está en `_instances`, se devuelve la referencia guardada; si no, se crea una instancia y se almacena.

Rol del `lock`:
- Garantiza que sólo un hilo entre a la sección crítica de creación de instancias.
- Evita crear múltiples instancias simultáneas en ejecuciones paralelas (condición de carrera).

## 2. Factory
`NullResourceFactory.create` encapsula la construcción de un bloque Terraform compatible (un dict) para `null_resource`. Los `triggers` en Terraform son usados para forzar recreación o para llevar metadatos que hacen que el recurso cambie cuando su contenido cambia (por ejemplo, incluir un UUID o timestamp). La fábrica centraliza formato, valores por defecto y lógica de metadatos.

## 3. Prototype
El patrón Prototype usa `deepcopy` para clonar el template original y producir instancias independientes. El `mutator` es una función callable que recibe la copia y la modifica (renombrar recursos, añadir bloques, cambiar triggers). Esto permite crear múltiples variantes partiendo de una plantilla base sin rehacer la construcción desde cero.

Diagrama (simplificado):
- ResourcePrototype -> (template) --deepcopy()--> copia independiente --mutator()--> instancia final

## 4. Composite
`CompositeModule` mantiene una lista `children` con bloques (cada uno puede contener `resource` o `module`). Al exportar, itera los hijos y fusiona recursivamente recursos por tipo (por ejemplo, `null_resource`) y módulos en una única estructura JSON válida para Terraform. Esto permite componer submódulos y recursos individuales en un único fichero de exportación.

## 5. Builder
`InfrastructureBuilder` orquesta:
- Factory: crea una plantilla base de recurso.
- Prototype: clona la plantilla y aplica mutators para personalizar cada instancia.
- Composite: agrupa las instancias clonadas.
Finalmente `export()` serializa el JSON con `json.dump()` a `terraform/main.tf.json`.

Diagrama general:
Factory -> Prototype -> Composite -> Builder (exporta JSON)

---

Archivos de diagrama (PlantUML) adjuntos en la carpeta `Fase1/`.


┌─────────────────────────┐        ┌────────────────────────────┐
│ SingletonMeta           │◄────── │ ConfigSingleton            │
│  _instances             │        │  env_name, settings        │
│  _lock                  │        │  reset()                   │
└─────────────────────────┘        └────────────────────────────┘
             ▲
             │
┌──────────────────────────────┐
│ NullResourceFactory          │◄───────┐
│  create(name, triggers)      │        │
└──────────────────────────────┘        │
             ▲                          │
┌────────────────────────────────────┐  │
│ TimestampedNullResourceFactory     │──┘
│  create(name, fmt)                 │
└────────────────────────────────────┘

┌──────────────────────────────┐
│ ResourcePrototype            │
│  clone(mutator)              │
└──────────────────────────────┘

┌──────────────────────────────┐
│ CompositeModule              │
│  add(block), export()        │
└──────────────────────────────┘

┌──────────────────────────────┐
│ InfrastructureBuilder        │
│  build_null_fleet(), export()│
└──────────────────────────────┘



