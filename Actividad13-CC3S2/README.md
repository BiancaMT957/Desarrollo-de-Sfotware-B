# Actividad13-CC3S2 — Entregable

## Estructura entregada

Actividad13-CC3S2/
- modules/simulated_app/
  - network.tf.json 
  - main.tf.json     
- environments/
  - app1/
    - network.tf.json
    - main.tf.json
  - app2/
    - network.tf.json
    - main.tf.json
  - env3/
    - network.tf.json  
    - main.tf.json
- legacy/
  - config.cfg
  - run.sh
- generate_envs.py   
- scripts/gitops_regenerate.sh
- .pre-commit-config.yaml
- .gitignore

## Cómo se usa

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

## Resumen de la Fase 1 – Respuestas principales

** ¿Cómo interpreta Terraform el cambio de una variable?
Terraform compara la configuración actual (archivos .tf.json y variables definidas) con el estado guardado del entorno.
Cuando una variable cambia y forma parte de los triggers o de los atributos que identifican al recurso, Terraform detecta esa diferencia y la marca en el plan.
En este caso, las variables están expuestas como triggers.* dentro de un null_resource, por lo que modificar el valor de network genera un cambio en triggers.network.

** ¿Qué diferencia hay entre modificar la plantilla JSON y editar directamente un recurso?
Lo correcto es modificar la plantilla fuente, por ejemplo modules/simulated_app/network.tf.json, ya que esa plantilla actúa como “fuente de verdad” y permite regenerar los entornos de forma coherente.
En cambio, editar manualmente un archivo de entorno como environments/app1/main.tf.json genera un cambio local no controlado (out-of-band).
Terraform detectará esa diferencia (“drift”) y tratará de corregirla según la plantilla o las variables originales.
Por eso, cambiar la plantilla garantiza consistencia, mientras que parchear directamente rompe ese flujo y obliga a reconciliar los cambios manualmente.

** ¿Por qué Terraform actualiza el recurso en lugar de recrearlo?
Terraform decide entre actualizar (in-place) o recrear un recurso según los atributos modificados.
Si el cambio no afecta la identidad del recurso (por ejemplo, un ajuste en los triggers de un null_resource), el sistema puede aplicar el cambio sin destruir ni volver a crear todo el recurso.
Esto optimiza la ejecución y evita recreaciones innecesarias.

** ¿Qué sucede si editas directamente main.tf.json en lugar de usar la plantilla?
Editar el archivo de entorno modifica localmente la configuración.
Terraform mostrará esa diferencia frente al estado y, dependiendo del caso, propondrá revertir o mantener los cambios.
Sin embargo, si más adelante regeneras el entorno a partir de la plantilla, ese cambio manual será sobrescrito.
Por eso, lo recomendable es siempre actualizar la plantilla y luego regenerar.

##  Resumen de la Fase 4 – Preguntas abiertas

** ¿Cómo escalarías el patrón a 50 módulos y 100 entornos?

Automatizar la generación y validación de configuraciones (terraform plan) usando pipelines de CI/CD.

Diseñar un catálogo central de módulos parametrizados (registry interno).

Estandarizar la convención de nombres y metadatos para mejorar la trazabilidad.

Usar backends remotos para manejar el estado y ejecutar verificaciones automáticas de drift (cambios no sincronizados).

** ¿Qué prácticas aplicarías para revisar los archivos .tf.json?

Validaciones automáticas en pre-commit o en CI usando jq y jsonschema.

Revisiones por Pull Request que incluyan terraform validate y terraform plan.

Mantener commits claros y separados: uno para valores por defecto (default) y otro para descripciones o metadatos.

** ¿Cómo manejar secretos en producción sin usar Vault?

Utilizar secrets managers del entorno (por ejemplo, KMS o almacenamiento protegido).

Inyectar variables seguras desde el pipeline de CI/CD, sin versionarlas.

En caso de almacenarlas, usar cifrado con herramientas como git-crypt o SOPS.

Evitar incluir secretos en los .tf.json; solo deben incorporarse al momento de ejecución.

** ¿Qué flujo de revisión aplicarías a los JSON generados?

No versionar los archivos generados, solo las plantillas y el generador.

Si es necesario incluirlos, validar automáticamente su formato y su consistencia mediante terraform validate y plan.

Implementar hooks y pruebas automáticas para garantizar la calidad y coherencia antes de hacer merge.

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

