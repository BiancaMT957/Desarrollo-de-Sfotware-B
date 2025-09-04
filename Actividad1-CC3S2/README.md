
# Actividad 1: Introducción a DevOps y DevSecOps  

**Nombre:** [Bianca Merhán Torres]  
**Fecha:** 30-08-2025  
**Tiempo invertido:** 03:10  

**Contexto del entorno:**  
Para el desarrollo de esta actividad utilicé un navegador web (Chrome) junto con herramientas en línea gratuitas como **draw.io** y **Excalidraw** para la elaboración de diagramas. Para la parte de evidencias prácticas (HTTP, DNS, TLS y puertos) empleé herramientas estándar accesibles desde el sistema operativo y verificadores en línea, cuidando siempre de no exponer información sensible.  

## 4.1 DevOps vs. Cascada tradicional
- **Comparación:** DevOps acelera el feedback y reduce riesgos mediante despliegues pequeños y continuos. Cascada se basa en entregas tardías y grandes lotes.  
- **Diagrama:**  
  ![Comparativa DevOps vs Cascada](imagenes/devops-vs-cascada.png)  
- **Caso donde cascada es razonable:** proyectos con certificación regulatoria estricta (ejemplo: software médico).  
  - Criterios: *cumplimiento normativo obligatorio* y *validación previa de hardware*.  
  - Trade-off: velocidad reducida a cambio de conformidad y seguridad.

---

## 4.2 Ciclo tradicional de dos pasos y silos
- **Limitaciones:** grandes lotes de cambios, acumulación de defectos.  
- **Anti-patrones:**  
  1. *Throw over the wall* → Handoff sin retroalimentación → Aumenta MTTR.  
  2. Seguridad como auditoría tardía → Costo de integración tardía.  
- **Diagrama:**  
  ![Silos organizacionales](imagenes/silos-equipos.png)

---

## 4.3 Principios y beneficios de DevOps
- **CI/CD:** Cambios pequeños, pruebas automatizadas y colaboración continua.  
- **Agile:** Retrospectivas influyen en decisiones del pipeline.  
- **Indicador observable:** Tiempo desde PR listo → despliegue en entorno de pruebas.  
  - Medición: metadatos de PR y registros de despliegue.  

---

## 4.4 Evolución a DevSecOps
- **SAST vs DAST:**  
  - *SAST:* análisis estático, temprano.  
  - *DAST:* dinámico, en ejecución.  
- **Puerta mínima de seguridad:**  
  - Bloqueo con hallazgos críticos en componentes expuestos.  
  - Cobertura mínima: ≥ 80% de pruebas de seguridad.  
- **Excepción:** válida por 14 días, responsable asignado, plan de corrección definido.  
- **Evitar “teatro de seguridad”:**  
  - Métricas: disminución de hallazgos repetidos y reducción del tiempo de remediación.

---

## 4.5 CI/CD y estrategias de despliegue
- **Estrategia elegida:** Canary release para microservicio de autenticación.  
- **Diagrama:**  
  ![Pipeline Canary](imagenes/pipeline_canary.png)  
- **Tabla de riesgos y mitigaciones:**

| Riesgo | Mitigación |
|--------|------------|
| Regresión funcional | Validación de contrato antes de promover |
| Costo operativo del doble despliegue | Límites de tiempo de convivencia |
| Manejo de sesiones | Draining y compatibilidad de esquemas |

- **KPI primario:** Latencia p95 ≤ 200ms (ventana 15 min).  

---

## 4.6 Evidencia práctica

### HTTP
- Método: GET  
- Código: 200  
- Cabeceras: `cache-control`, `x-trace-id`.  
![HTTP evidencia](imagenes/http-evidencia.png)  
*Impacto:* cache-control mejora rendimiento; x-trace-id da observabilidad.

### DNS
- Registro: A  
- TTL: 300 seg  
![DNS TTL](imagenes/dns-ttl.png)  
*Impacto:* TTL bajo facilita rollbacks, TTL alto retrasa propagación.

### TLS
- CN/SAN: dominio.com  
- Vigencia: 01/09/2025 – 01/12/2025  
- Emisora: Let’s Encrypt  
![TLS Certificado](imagenes/tls-cert.png)  
*Impacto:* si no valida → errores de confianza y riesgo MITM.

### Puertos
- En escucha: 80 (HTTP), 5432 (PostgreSQL)  
![Puertos](imagenes/puertos.png)  
*Impacto:* evidencia despliegue correcto; si puerto no está expuesto → fallo.

---

## 4.7 Desafíos de DevOps
- **Diagrama:**  
  ![Desafíos DevOps](imagenes/desafios_devops.png)  
- **Riesgos y mitigaciones:**  
  1. Riesgo cultural → Mitigación: revisión cruzada.  
  2. Riesgo técnico → Mitigación: despliegue gradual.  
  3. Riesgo de gobernanza → Mitigación: límites de blast radius.  
- **Experimento controlado:**  
  - Métrica primaria: tasa de errores.  
  - Grupo control: despliegue big-bang.  
  - Éxito: ≤ 50% errores comparado al control.  
  - Plan de reversión: rollback inmediato.

---

## 4.8 Arquitectura mínima DevSecOps
- **Diagrama:**  
  ![Arquitectura mínima](imagenes/arquitectura-minima.png)  
- **Flujo:** Cliente → DNS → HTTP → TLS → Servicio.  
- **Controles:** caché, validación certificados, contratos de API, rate-limits.  
- **Principios 12-Factor:**  
  - Config por entorno → reproducibilidad.  
  - Logs a stdout → trazabilidad sin rotación manual.

---

## Checklist de diagnóstico (incidente simulado)
1. **HTTP contrato** → verificar código 200.  
   - Evidencia: error 5xx → revisar logs.  
2. **Cabeceras HTTP** → verificar caché.  
   - Evidencia: ausencia → revisar configuración.  
3. **DNS** → revisar TTL/propagación.  
   - Evidencia: registros inconsistentes → esperar TTL o corregir.  
4. **TLS** → verificar vigencia/cadena.  
   - Evidencia: certificado caducado → renovar.  
5. **Puertos** → verificar servicio en escucha.  
   - Evidencia: puerto cerrado → revisar despliegue.  
6. **Logs de aplicación** → revisar flujo stdout.  
   - Evidencia: error recurrente → rollback.

---
