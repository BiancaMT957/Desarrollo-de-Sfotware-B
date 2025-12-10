# Logs con Loki y LogQL

## Expresiones LogQL utilizadas

### 1. Consulta base para ver todos los logs de la aplicación
```logql
{job="demo-app"}
```
### 2. Filtrado de logs por errores
{job="demo-app"} |= "ERROR"


Se utiliza para mostrar únicamente los eventos con nivel de severidad ERROR.

### 3. Filtrado por endpoint de error
{job="demo-app"} |= "/api/v1/error"


Permite identificar logs asociados al endpoint que genera errores 500.

### 4. Filtrado por advertencias
{job="demo-app"} |= "WARNING"


Se utiliza para detectar advertencias relacionadas con peticiones lentas.

Ejemplo de línea de log de error

Ejemplo real observado en los logs

```
2025-12-10 10:16:16.641	
2025-12-10 15:16:16,476 ERROR Simulated error endpoint called
2025-12-10 10:16:13.380	
2025-12-10 15:16:13,237 ERROR Simulated error endpoint called
2025-12-10 10:16:10.119	
2025-12-10 15:16:09,902 ERROR Simulated error endpoint called
2025-12-10 10:16:05.855	
2025-12-10 15:16:05,832 ERROR Simulated error endpoint called
2025-12-10 10:14:54.146	
2025-12-10 15:14:54,030 ERROR Simulated error endpoint called
2025-12-10 10:14:50.133	
2025-12-10 15:14:50,126 ERROR Simulated error endpoint called
2025-12-10 10:14:31.323	
2025-12-10 15:14:31,138 ERROR Simulated error endpoint called
2025-12-10 10:14:27.313	
2025-12-10 15:14:27,071 ERROR Simulated error endpoint called
2025-12-10 10:14:23.802	
2025-12-10 15:14:23,687 ERROR Simulated error endpoint called
2025-12-10 10:14:20.291	
2025-12-10 15:14:20,264 ERROR Simulated error endpoint called
```

Este log indica que el endpoint /api/v1/error fue ejecutado correctamente, pero devolvió un error interno del servidor (HTTP 500).

Uso de los logs en un contexto DevSecOps

En un entorno DevSecOps, los logs son fundamentales para la seguridad, el monitoreo y la respuesta a incidentes. Algunos usos clave son:

Detección temprana de fallos: Permiten identificar errores recurrentes antes de que impacten a los usuarios.

Análisis de seguridad: Ayudan a detectar patrones sospechosos como accesos repetidos, intentos de explotación o peticiones anómalas.

Monitoreo del rendimiento: A través de advertencias (WARNING) se pueden identificar cuellos de botella o peticiones lentas.

Respuesta a incidentes: Facilitan la reconstrucción de los eventos ocurridos durante un incidente.

Auditoría: Sirven como evidencia para revisiones de seguridad y cumplimiento.

La integración de Loki con Grafana permite correlacionar estos logs con métricas de Prometheus y trazas de Tempo, mejorando la observabilidad completa del sistema.