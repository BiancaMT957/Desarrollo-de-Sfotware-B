# Ejercicio 2.2 — Variación de la Factory

Rama sugerida: `feature/ejercicio-2-2-timestamped-factory`

Implementación:
- `TimestampedNullResourceFactory.create(name, fmt, extra=None)` genera triggers con `timestamp_formatted` usando `strftime(fmt)`.

Validación manual:
1. Usar el factory para crear el bloque y guardarlo como JSON:
   ```python
   from Actividad14_CC3S2.Fase2.Ejercicio2.2.factory import TimestampedNullResourceFactory
   block = TimestampedNullResourceFactory.create("app", "%Y%m%d")
   import json; print(json.dumps(block, indent=2))