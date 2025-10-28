# Actividad13-CC3S2 — Entregable

Este directorio contiene los entregables de la actividad sobre escribir infraestructura como código en un entorno local con Terraform.

## Estructura entregada

Actividad13-CC3S2/
- modules/simulated_app/
  - network.tf.json  (plantilla: `network` por defecto -> "lab-net", variable `port`, `api_key` sensible)
  - main.tf.json     (recurso `null_resource` renombrado a `local_server`)
- environments/
  - app1/
    - network.tf.json
    - main.tf.json
  - app2/
    - network.tf.json
    - main.tf.json
  - env3/
    - network.tf.json  (depende de `net2` simulando `net2-peered`)
    - main.tf.json
- legacy/
  - config.cfg
  - run.sh
- generate_envs.py         (genera entornos, lee API_KEY desde env o ~/.config/secure.json, CLI con click si está instalado)
- scripts/gitops_regenerate.sh
- .pre-commit-config.yaml
- .gitignore

## Cómo usar (rápido)

1. Colocar los archivos en tu repositorio bajo `Actividad13-CC3S2/`.
2. (Opcional) Crear `~/.config/secure.json` con:
   ```json
   {
     "api_key": "TU_API_KEY_AQUI"
   }
   ```
   O exportar la variable:
   ```bash
   export API_KEY="TU_API_KEY_AQUI"
   ```
3. Generar entornos:
   ```bash
   cd Actividad13-CC3S2
   python3 generate_envs.py
   ```
   O con opciones:
   ```bash
   python3 generate_envs.py --count 3 --prefix staging- --start-port 3000
   ```
4. Probar un entorno:
   ```bash
   cd environments/app1
   terraform init
   terraform plan
   ```
   Deberías ver triggers que usan `network` y `port`. Si modificas `modules/simulated_app/network.tf.json` y regeneras, `terraform plan` en el entorno reflejará el cambio en los triggers.

## Respuestas a las preguntas de la Fase 1 (resumen)

- ¿Cómo interpreta Terraform el cambio de variable?
  Terraform compara la configuración actual (archivos .tf.json y variables) con el estado remoto/local. Si el cambio de variable afecta a los valores que se usan como triggers o atributos que forman parte de la identidad del recurso, Terraform lo muestra como una diferencia. En este ejercicio las variables se exponen como `triggers.*` en el `null_resource`, por lo que cambiar `network` produce una diferencia en `triggers.network`.

- ¿Qué diferencia hay entre modificar el JSON vs. parchear directamente el recurso?
  Modificar la plantilla (p. ej. `modules/simulated_app/network.tf.json`) es la vía correcta: la plantilla es la fuente de verdad y permite regenerar los entornos automáticamente. Parchear un recurso en un entorno concreto (`environments/app1/main.tf.json`) es un cambio local y "out-of-band": Terraform detectará ese "drift" y propondrá revertirlo si la plantilla (o las variables) indican otro valor. Cambiar la plantilla y regenerar mantiene consistencia; parchear rompe esa disciplina y obliga a reconciliación manual.

- ¿Por qué Terraform no recrea todo el recurso, sino que aplica el cambio "in-place"?
  Terraform decide si un cambio requiere recreación o puede aplicarse in-place según qué atributos del recurso cambian y si esos atributos son parte de la llave/identidad del recurso según el proveedor. En el caso de `null_resource` con `triggers`, se trata de una actualización de metadatos que provoca la ejecución de acciones (ej. `provisioner`), pero no siempre requiere destruir y volver a crear el recurso si la implementación permite cambio en-situ.

- ¿Qué pasa si editas directamente `main.tf.json` en lugar de la plantilla de variables?
  Editar `main.tf.json` en un entorno es un cambio local: terraform detectará la diferencia frente al estado y, dependiendo del cambio, propondrá revertirla o modificar el recurso. Si luego vuelves a regenerar desde la plantilla, tu parche local será sobrescrito (si tu script lo hace). Por eso es preferible siempre cambiar la plantilla y regenerar.

## Respuestas a las preguntas abiertas de la Fase 4 (resumen)

- ¿Cómo extenderías este patrón para 50 módulos y 100 entornos?
  - Automatizar generación y testing (CI) para validar `terraform plan` en entornos simulados.
  - Usar plantillas parametrizadas y un catálogo de módulos (registry interno).
  - Centralizar naming convention y metadatos para facilitar búsqueda y reglas.
  - Controlar estado con backends (si se pasa a nube), y manejar drift con jobs automáticos.

- ¿Qué prácticas de revisión de código aplicarías a los `.tf.json`?
  - Validación automática con `jq` y `jsonschema` en pre-commit / CI.
  - Revisiones en Pull Requests con checks que ejecuten `terraform validate`/`plan`.
  - Mensajes de commit claros y separación de cambios: `default` vs `description` en commits distintos.

- ¿Cómo gestionarías secretos en producción (sin Vault)?
  - Usar mecanismos de secrets manager (KMS + storage protegido), variables de entorno inyectadas en CI/CD, o archivos fuera del repo (ej. `~/.config/secure.json`) con acceso restringido.
  - Encriptar secretos en repositorio si se necesita (e.g., git-crypt, SOPS).
  - Minimizar exposición: no escribir secretos en los archivos `.tf.json` versionados; inyectarlos en tiempo de ejecución.

- ¿Qué workflows de revisión aplicarías a los JSON generados?
  - No versionar archivos generados; versionar plantillas y el generador.
  - Si es necesario versionar entornos, validar con CI que el JSON cumpla esquema y que `terraform plan` no muestre cambios inesperados.
  - Hooks pre-commit y pipelines que validen formato y esquema.

## Ejercicios implementados en este entregable

- Cambio del `default` de `network` a `"lab-net"` en `modules/simulated_app/network.tf.json`.
- Renombrado del recurso `null_resource` a `local_server` en los `main.tf.json`.
- Añadida variable `port` y lectura de `api_key` desde entorno o `~/.config/secure.json`.
- Script `generate_envs.py` que genera `app1`, `app2`, `env3` y soporta opciones CLI si `click` está instalado.
- Script `scripts/gitops_regenerate.sh` para regenerar envs desde las plantillas.
- `pre-commit` hook para chequear JSON con `jq` (config).

## Notas finales y recomendaciones

- No incluyas `~/.config/secure.json` en el repo; usar `.gitignore` y documentar su uso.
- Para pruebas locales, instala `jq` para formateo y validación rápida.
- Si quieres, puedo:
  - Preparar un branch con estos archivos ya añadidos y commits con los mensajes solicitados.
  - Ajustar los contenidos (por ejemplo cambiar puertos, nombres, o la forma en que se inyecta `api_key`).
  - Generar scripts adicionales (ej. JSON Schema y validación con `jsonschema`).
