# Actividad 5 – Makefile, Reproducibilidad y Pruebas

## Resumen del entorno
Sistema operativo: Ubuntu 22.04 sobre WSL2 / Windows 10.  
Shell: bash 5.1.  
Make: GNU Make 4.3.  
Python3: 3.11.4 (por defecto) y Python 3.12 probado opcionalmente.  
Tar: GNU tar 1.34.  
sha256sum: disponible para verificación de integridad.  
TZ=UTC para asegurar reproducibilidad determinista de paquetes.

---

## Parte 1 – Construir
El objetivo `build` genera `out/hello.txt` ejecutando `$(PYTHON) $< > $@`.  
Aquí `$<` es la primera dependencia (`src/hello.py`) y `$@` es el objetivo (`out/hello.txt`), redirigiendo la salida del script al archivo.  
El Makefile usa modo estricto (`-e -u -o pipefail`) y `.DELETE_ON_ERROR` para evitar artefactos parciales si ocurre un fallo.  
En la primera corrida, `hello.txt` se crea; en la segunda, Make detecta que la fuente no cambió y no rehace nada, demostrando idempotencia gracias a marcas de tiempo y grafo de dependencias.

---

## Parte 2 – Leer
Con `make -n` se muestran los comandos que se ejecutarían sin correrlos; `make -d` permite analizar decisiones sobre rehacer objetivos.  
Make reconstruye solo objetivos que necesitan actualización, evaluando timestamps y dependencias.  
`.DEFAULT_GOAL := help` asegura que `make` sin argumentos muestre ayuda, y `.PHONY` evita conflictos con archivos.  
La ayuda autodocumentada extrae comentarios `##` para cada objetivo, facilitando la operación y onboarding.

---

## Parte 3 – Extensor

### Lint y Formato
`make lint` detecta problemas de quoting con shellcheck; si shfmt está disponible, `make format` normaliza estilo.  
Si ruff no está instalado, Make lo omite sin romper la construcción, mostrando evidencia de su ausencia.

### Rollback y trap
Al romper temporalmente un archivo y ejecutar `scripts/run_tests.sh`, el trap restaura `hello.py` y devuelve un código de salida no cero.  
Esto asegura que los errores no corrompan el entorno y que el estado original se preserve automáticamente.

### Reproducibilidad
Paquetes generados con `make package` usan flags deterministas: `--sort=name`, `--numeric-owner`, `--owner=0`, `--group=0`, `--mtime='UTC 1970-01-01'`.  
`make verify-repro` confirma que los SHA256 coinciden en corridas consecutivas, asegurando que la construcción sea reproducible.  
El uso de TZ=UTC y control de metadatos evita diferencias entre máquinas o ejecuciones.

### Incidencias y mitigaciones
Problemas detectados: errores de quoting en scripts, ausencia de ruff, y advertencias de shellcheck.  
Se corrigieron quotes, se documentó la ausencia de herramientas opcionales, y se verificó build limpio tras `make dist-clean`.

---

## Conclusión operativa
El pipeline garantiza builds reproducibles, tests automáticos y lint/formato integrados, lo que permite su uso confiable en CI/CD.  
La combinación de dependencias precisas, manejo de errores y rollback asegura integridad del código y consistencia entre entornos.
