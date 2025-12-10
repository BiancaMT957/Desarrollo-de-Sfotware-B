Grafana Alerting – Actividad 22

Esta sección documenta la regla de alerta creada en Grafana basada en errores HTTP 5xx detectados por Prometheus.

## 1. Métrica utilizada (PromQL)

La alerta está basada en la siguiente consulta:

sum(rate(http_server_requests_total{status_code=~"5.."}[5m])) by (service_name)

¿Qué mide esta métrica?

http_server_requests_total = total de requests HTTP del servicio.

status_code=~"5.." = filtra únicamente los errores 5xx (errores del servidor).

rate(...[5m]) = calcula la tasa de errores por segundo en una ventana de 5 minutos.

sum(...) by (service_name) = agrupa la tasa por servicio.

Esta métrica permite detectar cuando una aplicación comienza a devolver muchos errores críticos.

## 2. Condición de la alerta

La regla se evaluó con la siguiente lógica:

Cuando el resultado de la métrica (Reduce: Last)
sea mayor que 0.1
durante un período continuo de 5 minutos
→ Disparar la alerta.


En la interfaz nueva de Grafana esto se representó con:

Bloque Reduce

Input: A

Function: Last

Mode: Strict

Bloque Threshold

Input: B

IS ABOVE: 0.1

Pending period

5m

## 3. Etiquetas (Labels)

Se añadió el siguiente label para clasificación:

severity = "critical"

## 4. Mensaje de alerta

Se configuró el mensaje:

Summary

Exceso de errores HTTP 5xx


Description

La demo-app está devolviendo demasiados errores 5xx.

## 5. Justificación de la regla

Esta alerta permite detectar:

Fallos graves en el backend.

Picos de errores causados por bugs, mala implementación o sobrecarga.

Condiciones que pueden causar caída del servicio.

Problemas que deben atenderse de inmediato en un proceso DevSecOps.

Configurar una alerta basada en errores 5xx es fundamental para garantizar disponibilidad, estabilidad y detección temprana de fallas críticas en un ambiente de observabilidad.

## 6. Estado final

La alerta se creó correctamente en:

Alerting → Alert rules → (Actividad22 / grupo-actividad22)
Y quedó guardada en Grafana con los parámetros requeridos.