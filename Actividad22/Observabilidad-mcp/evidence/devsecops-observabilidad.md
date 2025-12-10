# DevSecOps y Observabilidad – Actividad 22

## 1. Introducción

La observabilidad permite monitorear el comportamiento de las aplicaciones en tiempo real mediante métricas, logs y trazas. En un enfoque DevSecOps, esta información no solo se utiliza para visualizar el estado del sistema, sino también para aplicar controles automáticos de calidad, seguridad y estabilidad durante el ciclo de vida del software.

En esta actividad se integraron herramientas como Prometheus, Grafana y Loki para implementar observabilidad en una demo-app, y a partir de estas métricas se definieron gates automáticos para reforzar el pipeline DevSecOps.

---

## 2. Rol de la observabilidad en DevSecOps

La observabilidad apoya directamente a DevSecOps en los siguientes aspectos:

- Detección temprana de fallos en producción.
- Monitoreo continuo de la estabilidad del servicio.
- Prevención de despliegues defectuosos.
- Identificación de patrones sospechosos en los logs.
- Validación objetiva de la salud del sistema antes de liberar versiones.

Gracias a las métricas y logs, los equipos pueden tomar decisiones automáticas en los pipelines CI/CD sin depender únicamente de pruebas manuales.

---

## 3. Gates DevSecOps definidos para la demo

Se definieron los siguientes **gates automáticos**, con umbrales realistas para un entorno de pruebas:

---

###  Gate 1 – Error rate HTTP 5xx (Estabilidad)

**Métrica usada:**

```promql
sum(rate(http_server_requests_total{status_code=~"5.."}[5m]))
```
Threshold:

Si la tasa de errores 5xx es mayor a 0.1 errores/segundo durante 5 minutos, el despliegue se bloquea.

Acción del gate:

El pipeline CI/CD detiene el despliegue a producción.

Se genera una alerta crítica en Grafana.

El equipo debe revisar errores de backend antes de continuar.

Justificación:
Un nivel sostenido de errores 5xx indica fallos graves del servidor que comprometen la disponibilidad del servicio.

### Gate 2 – Disponibilidad del servicio (Uptime)

Métrica usada:

up == 1


Threshold:

Si el valor es distinto de 1 por más de 2 minutos, el servicio es considerado caído.

Acción del gate:

Se impide publicar una nueva versión.

Se activa una alerta automática de servicio caído.

Se exige verificación del contenedor o infraestructura.

Justificación:
Garantiza que solo se despliegan nuevas versiones cuando el sistema se encuentra activo y estable.

### Gate 3 – Logs de error crítico (Seguridad y estabilidad)

Consulta LogQL:

{job="demo-app"} |= "ERROR"


Threshold:

Más de 10 errores críticos en 5 minutos.

Acción del gate:

Se bloquea el pipeline.

Se marca el build como inestable.

Se exige revisión del código o configuración.

Justificación:
Un volumen alto de errores en los logs puede indicar:

fallos internos,

problemas de conexión,

vulnerabilidades,

o malas configuraciones.

Este gate mejora tanto la estabilidad como la seguridad del sistema.

## 4. Uso de observabilidad en un contexto DevSecOps

En un entorno DevSecOps real, los logs y métricas se emplean para:

Detectar accesos sospechosos.

Identificar intentos de ataque por fuerza bruta.

Rastrear errores repetitivos por vulnerabilidades.

Validar que una versión nueva no degrade el rendimiento.

Auditar eventos críticos para cumplimiento de seguridad.

La observabilidad se convierte así en una capa activa de seguridad continua.

## 5. Conclusión

La integración de observabilidad con gates DevSecOps permite convertir métricas y logs en controles automáticos de calidad y seguridad. En esta actividad se demostró cómo Prometheus, Grafana y Loki pueden utilizarse no solo para monitoreo visual, sino también como base para decisiones automáticas en pipelines CI/CD.

Esto fortalece la detección temprana de fallos, reduce riesgos en producción y mejora la confiabilidad de los despliegues.


