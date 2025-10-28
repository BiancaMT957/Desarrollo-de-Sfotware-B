# Ejercicio 2.3 — Mutaciones avanzadas con Prototype

Rama sugerida: `feature/ejercicio-2-3-prototype-localfile`

Implementación:
- `ResourcePrototype.clone(mutator)` como en el patrón.
- Mutator `add_welcome_file` añade un trigger y un bloque `local_file`.

Validación:
1. Clona el template, aplica `add_welcome_file`, agrega al builder y exporta JSON.
2. Ejecuta `terraform apply` para confirmar que `bienvenida.txt` se crea (suponiendo que `local_file` provider está disponible en el entorno).