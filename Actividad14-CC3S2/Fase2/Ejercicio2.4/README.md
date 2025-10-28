# Ejercicio 2.4 — Submódulos con Composite

Rama sugerida: `feature/ejercicio-2-4-composite-submodules`

Implementación:
- `CompositeModule.add()` acepta bloques con `module` y `resource`.
- `export()` ahora devuelve `{"module": {...}, "resource": {...}}` (si aplica).

Validación:
1. Crear dos submódulos:
   - network -> resources de red
   - app -> recursos de la aplicación
2. Añadir ambos usando `module` (ver ejemplo en `Ejercicio2.5` builder).
3. Ejecutar `terraform validate` sobre el JSON resultante.