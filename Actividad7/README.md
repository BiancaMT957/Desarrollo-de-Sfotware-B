
# Actividad 7 - Estrategias de fusión en Git

## A) Evitar (o no) `--ff`
**¿Cuándo evitarías `--ff` en un equipo y por qué?**
→ Cuando se requiere trazabilidad de merges, auditorías o trabajo colaborativo, ya que `--ff` oculta la existencia de ramas.

## B) Trabajo en equipo con `--no-ff`
- **Ventajas:** Preserva el punto de integración, se puede auditar qué rama fue integrada.
- **Problemas:** Si hay demasiados merges, el DAG se vuelve muy complejo.

## C) Squash
- **Cuándo conviene:** Para mantener el historial limpio en `main`, integrando muchas pruebas internas en un solo commit.
- **Qué se pierde:** El detalle de commits intermedios (no quedan enlazados en el DAG).

## d) Conflictos reales con no-fast-forward
- ¿Qué pasos adicionales hiciste para resolverlo? detectar conflicto, usar git diff, resolver marcadores <<<<<<< >>>>>>>, hacer commit.

- ¿Qué prácticas (convenciones, PRs pequeñas, pruebas) lo evitarían?
 PRs pequeños, revisiones frecuentes, pruebas automáticas.

## Comparar historiales tras cada método

#### ¿Cómo se ve el DAG en cada caso? 
Fast-Forward (FF)
main: o---o---o

No-Fast-Forward (No-FF)
main: o---o
        \
feature:  o---o
merge:    *

Squash
main: o---*   (todos los commits feature aplastados en *)
feature: o---o---o (permanecen en la rama feature)


#### ¿Qué método prefieres para: trabajo individual, equipo grande, repos con auditoría estricta?

- Para trabajo individual prefiero **fast-forward** porque da un historial limpio y lineal.
- Para un equipo grande prefiero **no-fast-forward**, ya que deja visible en qué punto se integraron ramas y facilita auditoría del trabajo colaborativo.
- Para repos con auditoría estricta prefiero **no-fast-forward o squash con firmas GPG**, porque aseguran trazabilidad, cumplimiento y un historial que puede ser revisado fácilmente en procesos de CI/CD o auditorías externas.

## ¿Cuándo usar git revert en vez de git reset?

Revert es seguro en repos públicos, no reescribe historia.

Reset cambia historia y puede romper repos compartidos.

Impacto: mantiene historial público consistente, evita confusiones en equipos.

## Variantes útiles para DevOps/DevSecOps

Estas estrategias avanzadas de fusión permiten controlar mejor el flujo de trabajo, la trazabilidad y la calidad del código en equipos grandes y entornos con requisitos de auditoría.

| Variante | Objetivo | Uso en DevOps/DevSecOps | Ventajas | Limitaciones |
|----------|----------|--------------------------|----------|--------------|
| **09) `--ff-only`** | Evitar merges automáticos con commits innecesarios | Mantener `main` lineal en pipelines CI/CD | Historial limpio y seguro | Falla si no se puede hacer fast-forward |
| **10) Rebase + FF** | Reescribir commits para integrarlos de forma lineal | Usado en PRs para merges finales con `ff` | Historial claro y auditable | Reescribe commits, no apto para ramas compartidas |
| **11) `--no-commit --no-ff`** | Validar antes de confirmar la fusión | Ejecutar linters, tests o escáneres en hooks/pipelines | Garantiza calidad antes de mergear | Requiere pasos manuales o automatización extra |
| **12) Octopus Merge** | Integrar múltiples ramas en un solo commit | Útil para merges masivos triviales (docs, fixes) | Menos ruido en el historial | No soporta conflictos complejos |
| **13) Subtree** | Incluir proyectos completos preservando historial | Integrar librerías/microservicios internos | Independencia y trazabilidad | Puede duplicar historial si no se gestiona bien |
| **14) Estrategias `-X ours/theirs/renormalize`** | Controlar cómo resolver conflictos | Automatizar merges en pipelines (ej. preferir `main`) | Reduce intervención manual | Riesgo de perder cambios si no se audita |
| **15) Signed Merge** | Firmar merges con GPG o Sigstore | Cumplimiento en auditorías y seguridad del código | Autenticidad y trazabilidad garantizada | Requiere infraestructura de claves/firmas |

---
**Conclusión**  
- Para **proyectos individuales**: `--ff-only` o `rebase + ff`.  
- Para **equipos grandes**: `--no-ff` y `--squash` mejoran la trazabilidad.  
- En **DevOps/DevSecOps**: la validación previa, estrategias automatizadas y firmas criptográficas son clave para calidad y seguridad.  




