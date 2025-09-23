# Actividad 6 – Git: Cherry-Picking y Stash

## Comandos usados

- **git config** – Para configurar usuario y correo en Git:  
  ```bash
  git config --global user.name "BiancaMT957"
  git config --global user.email "merchantorresbianca75@gmail.com"
- **git init** - init – Para inicializar un repositorio vacío
  git add main.py
  git commit -m "Agrega ejemplo de cherry-pick"
- **add / commit** – Para preparar y guardar cambios
- **log** – Para revisar el historial de commits
- **Rama** – Crear, cambiar, fusionar y resolución de conflictos
  git checkout -b feature/cherry-pick
  git cherry-pick <commit-hash>
  Se resolvió conflicto con cherry-pick vacío usando:
  git cherry-pick --skip

- **git revert HEAD** → Revertí un commit que agregaba main.py.

- **git rebase -i HEAD~3** → Hice squash de tres commits en uno solo.

- **git cherry-pick f66f5b9** → Aplicación de commit específico en otra rama.

- **git stash** → Guardé cambios temporales y luego los recuperé con git stash pop

## Preguntas de reflexión

### 1. ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?
Git me ha permitido guardar cada cambio con mensajes claros y ver exactamente qué se modificó en cada commit, lo que facilita rastrear errores y revisar la evolución del proyecto.

### 2. ¿Qué ventajas ves en el uso de ramas para nuevas características o corrección de errores?
Las ramas permiten trabajar de manera aislada en nuevas funciones o correcciones sin afectar la rama principal (main o develop). Esto ayuda a probar y experimentar sin riesgos y luego fusionar los cambios de manera controlada.

### 3. Revisión del historial de commits
Al revisar git log, se puede comprobar que todos los cambios importantes están registrados: inicialización del repositorio, agregados de archivos (main.py, CONTRIBUTING.md), ejemplos de cherry-pick y revert de commits.

### 4. Experiencia resolviendo conflictos de fusión
Durante el rebase interactivo y el cherry-pick surgieron conflictos (por ejemplo, commits repetidos). Git indica exactamente qué pasos seguir (--skip, --continue) y permite combinarlos de manera ordenada, lo que facilita mantener un historial limpio.

  
