# Actividad 22 – Observabilidad en el Ciclo de Vida DevSecOps

##  Descripción de la actividad

En esta actividad se implementa un stack de observabilidad basado en **Prometheus, Grafana, Loki, Tempo y OpenTelemetry**, con el objetivo de monitorear métricas, analizar logs, visualizar trazas y aplicar principios DevSecOps mediante gates automáticos y alertas.

El entorno permite analizar el comportamiento de una aplicación demo, generar tráfico, visualizar métricas en tiempo real, crear dashboards y definir reglas de alertamiento.

---

##  Instrucciones para reproducir la actividad

### 1. Levantar el stack completo

Desde la raíz del proyecto ejecutar:

```bash
make up
```


Esto iniciará todos los servicios necesarios mediante Docker Compose.

### 2. Generar tráfico de prueba

Para simular peticiones a la demo-app:

make demo-traffic


O alternativamente:

./scripts/demo-traffic.sh


Esto permite que Prometheus, Loki y Grafana reciban datos reales.

### URLs de acceso

Una vez levantado el stack, se puede acceder a los servicios desde el navegador:

Aplicación demo:
http://localhost:8000/docs

Grafana:
http://localhost:3000

Prometheus:
http://localhost:9090

Servidor MCP:
http://localhost:8080/docs

### Evidencias generadas

Los resultados de la actividad se encuentran documentados en los siguientes archivos:

observabilidad-telemetria.md → Mapa conceptual y arquitectura.

metrics-prometheus.md → Consultas PromQL y métricas usadas.

logs-loki-logql.md → Consultas LogQL y ejemplos de logs.

tracing-tempo.md → Análisis de trazas.

grafana-alerting.md → Regla de alerta configurada en Grafana.

devsecops-observabilidad.md → Integración de observabilidad en DevSecOps.

dashboard-actividad22.json → Dashboard exportado desde Grafana.

### Buenas prácticas aplicadas

Uso de métricas estándar (up, http_server_requests_total).

Separación de métricas, logs y trazas.

Centralización del monitoreo en Grafana.

Implementación de alertas automáticas.

Definición de gates DevSecOps basados en observabilidad.

Documentación clara de cada parte del proceso.




