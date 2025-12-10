# Observabilidad y Telemetría

## 1. Definición de Observabilidad

La observabilidad es la capacidad de un sistema para comprender su estado interno a partir de la información que produce, como métricas, logs y trazas. Permite responder preguntas como:

- ¿El sistema está funcionando correctamente?
- ¿Dónde están ocurriendo los errores?
- ¿Qué componente genera más latencia?

La observabilidad no solo sirve para monitorear, sino también para diagnosticar y anticipar fallos.

---

## 2. Definición de Telemetría

La telemetría es el proceso de recolección automática de datos desde los sistemas hacia plataformas de análisis. Estos datos incluyen:

- Métricas (uso de CPU, memoria, peticiones)
- Logs (eventos y errores)
- Trazas (flujo completo de una petición)

La telemetría es la base que alimenta a las plataformas de observabilidad como Prometheus, Loki y Tempo.

---

## 3. Pilares de la Observabilidad

### a) Métricas
Son valores numéricos que representan el comportamiento del sistema a lo largo del tiempo.
Ejemplo:
- Cantidad de peticiones por segundo
- Uso de CPU
- Latencia de respuesta

Se recolectan con Prometheus.

---

### b) Logs
Son registros detallados de eventos que ocurren en el sistema.
Ejemplo:
- Peticiones HTTP
- Errores 500
- Advertencias (warning)

Se almacenan y procesan con Loki.

---

### c) Trazas (Tracing)
Permiten seguir una solicitud completa a través de múltiples servicios.
Ejemplo:
- Desde el navegador
- Pasando por la API
- Hasta la base de datos

Se gestionan con Tempo.

---

## 4. Stack de Observabilidad usado en la actividad

El stack implementado en esta actividad está conformado por:

- Aplicación demo (FastAPI)
- Prometheus (métricas)
- Loki (logs)
- Tempo (trazas)
- Grafana (visualización)
- Docker & Docker Compose (orquestación)

---

## 5. Diagrama del Stack de Observabilidad (ASCII)

```text
+--------------------+
|     Usuario        |
|   (Navegador)      |
+---------+----------+
          |
          v
+-----------------------------+
|        Aplicación Demo      |
|         (FastAPI)           |
+------+----------+-----------+
       |          |
       |          |
       v          v
+-------------+  +-------------+
|   Prometheus |  |    Loki     |
|   (Métricas) |  |   (Logs)    |
+-------------+  +-------------+
       |
       v
+-------------+
|    Tempo    |
|  (Traces)   |
+-------------+
       |
       v
+-----------------------------+
|           Grafana           |
| (Dashboards y Alertas)     |
+-----------------------------+
```

## 6. Importancia de la Observabilidad en DevOps y DevSecOps

En DevOps, la observabilidad permite:

Detectar errores rápidamente

Optimizar el rendimiento

Reducir el tiempo de respuesta ante incidentes

En DevSecOps, además:

Permite detectar comportamientos anómalos

Identificar patrones de ataque

Analizar incidentes de seguridad a través de logs y trazas

## 7. Conclusión

La observabilidad es un pilar fundamental en los sistemas modernos. Gracias a la integración de métricas, logs y trazas, es posible tener un control completo del estado de las aplicaciones. El uso de herramientas como Prometheus, Loki, Tempo y Grafana permite implementar observabilidad de forma centralizada y eficiente.

