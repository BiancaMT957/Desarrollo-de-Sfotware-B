# Ejercicio 2.1 — Extensión del Singleton

Rama sugerida: `feature/ejercicio-2-1-singleton-reset`
Ejemplo de commit:  abcdef1 (reemplazar por el hash real al subir)

Implementación:
- `ConfigSingleton.reset()` limpia `settings` manteniendo `created_at`.

Validación:
```python
from Actividad14-CC3S2.Fase2.Ejercicio2.1.singleton import ConfigSingleton

c1 = ConfigSingleton("dev")
created = c1.created_at
c1.settings["x"] = 1
c1.reset()
assert c1.settings == {}
assert c1.created_at == created