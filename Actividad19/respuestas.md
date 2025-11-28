#  Bloque 1 – Conceptualización de Microservicios

## 1. Evolución: Monolito → SOA → Microservicios

**Monolito**  
- Una sola aplicación, un solo despliegue, alto acoplamiento.  
- Problemas al crecer: despliegues lentos, interdependencias complejas, escalado rígido.

**SOA (Service-Oriented Architecture)**  
- Resuelve problemas del monolito mediante servicios con contratos definidos.  
- Problema típico: fuerte dependencia en un ESB centralizado → cuellos de botella y acoplamiento operativo.

**Microservicios**  
- Evolución natural de SOA.  
- Servicios pequeños, autónomos, con límites claros.  
- Despliegue independiente.  
- Reemplazan el ESB con comunicación ligera (REST/gRPC), contenedores y DevOps.

---

## 2. Casos donde el monolito se vuelve costoso

###  Caso 1: E-commerce con picos estacionales
- Módulos como catálogo o checkout necesitan escalar más.  
- En un monolito, **se replica todo**, generando costos y riesgos innecesarios.

###  Caso 2: Plataforma SaaS multi-tenant
- Personalizaciones por cliente afectan a todos.  
- Un despliegue impacta a toda la base de usuarios.

---

## 3. Definiciones esenciales

**Microservicio:**  
Unidad de despliegue independiente enfocada en una capacidad de negocio, normalmente expuesta por una API.

**Aplicación de microservicios:**  
Conjunto de microservicios que cooperan mediante:  
- API Gateway  
- Balanceadores  
- Monitoreo  
- Métricas  
- Logging  
- Trazabilidad distribuida  

---

## 4. Críticas al monolito

- **Cadencia lenta:** un cambio pequeño → redeploy completo.  
- **Escalado desigual:** no permite escalar módulos individuales.

---

## 5. Por qué grandes empresas adoptaron microservicios

- **Aislamiento de fallos**  
- **Escalado granular** por servicio  
- **Autonomía de equipos pequeños**  
- **Libertad tecnológica** entre servicios  

---

## 6. Desventajas y retos de los microservicios

- Mayor complejidad de red y seguridad  
- Necesidad de orquestadores (Docker Compose / Kubernetes)  
- Consistencia de datos no-ACID  
- Testing distribuido y costoso  

**Mitigaciones:**  
- Contratos claros (OpenAPI / Protobuf)  
- Contract Testing  
- Trazabilidad distribuida (Jaeger/Zipkin)  
- Patrones como Saga  

---

## 7. Principios de diseño

###  DDD (Domain-Driven Design)
- Definir *bounded contexts*.  
- Priorizar capacidades de negocio, no tablas técnicas.

###  DRY equilibrado
- Evitar dependencias compartidas.  
- Aceptar cierta duplicación si mejora la independencia.

###  Tamaño del microservicio
**Regla:**  
➡ *Una capacidad de negocio por servicio*.  
(Evitar dogmas como “una tabla por servicio”.)

---

##  Conclusiones del Bloque 1
Los microservicios ofrecen flexibilidad, escalabilidad y velocidad, pero agregan complejidad operativa.  
Requieren buen diseño con DDD, contratos sólidos y prácticas DevOps.  
Son ideales para organizaciones grandes o con alta demanda, pero no reemplazan al monolito en proyectos simples.

---

#  Bloque 2 – Empaquetado y Verificación con Docker

## 1. Dockerfile y multi-stage

Un Dockerfile multi-stage separa:

- **Build stage:** dependencias y compilación  
- **Runtime stage:** imagen final ligera  

**Beneficios:**
- Imágenes pequeñas  
- Menor superficie de ataque  
- Reproducibilidad  
- No incluye herramientas de build en producción  

**Buenas prácticas:**
- Usar usuario NO root  
- `PYTHONDONTWRITEBYTECODE=1`  
- `ENTRYPOINT` claro  

---

## 2. Imagen, etiquetas y SemVer

**Requisitos:**
- Nombre fijo: `ejemplo-microservice`  
- Tag basado en **SemVer**: `0.1.0`  

**No usar `latest`:**
- No determinístico  
- Oculta la versión real  
- Rompe integraciones  
- Afecta reproducibilidad en CI/CD  

**Ventajas de SemVer:**
- Reproducibilidad total  
- Seguimiento de cambios  
- Flujo claro dev → stage → prod  

---

## 3. SQLite como base obligatoria

**Ventajas en desarrollo:**
- Un solo archivo (`app.db`)  
- Sin servidor externo  
- Deploy simple dentro del contenedor  

**En producción sería mejor:**  
- PostgreSQL (concurrencia, replicación, ACID, eventos)

---

## 4. Pruebas (pytest -q)

Cobertura mínima:  
- `GET /api/items` → lista  
- `POST /api/items` → creación + persistencia  

Esto valida que:  
- El microservicio funciona  
- El Dockerfile y la imagen están correctamente configurados  

---

## Conclusiones del Bloque 2
Docker garantiza aislamiento, portabilidad y consistencia.  
SQLite simplifica el desarrollo inicial.  
SemVer reemplaza `latest` para manejo profesional de versiones.  
Pruebas con pytest validan la funcionalidad base y del contenedor.

---

#  Bloque 3 – Desarrollo y Despliegue (Bonus Opcional)

## 1. Docker Compose – teoría

**Permite:**
- Redes internas  
- Dependencias controladas  
- Perfiles (dev/test/prod)  
- Bind mounts para hot-reload  

**Casos útiles:**
- Staging local  
- Pruebas de integración  
- Recarga en vivo de código  

---

## 2. Comunicación entre servicios (REST / gRPC / MQs)

### REST vs gRPC
- **REST:** simple, legible, mayor latencia  
- **gRPC:** eficiente, basado en contratos, binario  

**Caso ideal para gRPC:**  
Operaciones financieras de baja latencia.

---

### RabbitMQ vs Kafka

- **RabbitMQ:** colas clásicas, tareas puntuales  
- **Kafka:** log distribuido, múltiples consumidores, retención  

**Kafka es superior para:**  
Eventos persistentes como *OrderCreated* o *PaymentProcessed*.

---

## 3. Pruebas con stubs

Aseguran resiliencia cuando otros servicios fallan:  
- Evitan caídas ante un 500  
- Evitan romper contratos entre servicios independientes  

---

## 4. Kubernetes – teoría

**Permite:**
- Autoescalado  
- Alta disponibilidad  
- Orquestación avanzada  

**Objetos clave:**
- Deployment  
- Service  
- Probes de salud  
- Carga de imágenes locales (kind/minikube)

---

## 5. CI/CD – flujo conceptual

Pipeline típico:
1. Build + etiqueta SemVer  
2. Pruebas con Compose  
3. Deploy a staging  
4. Rollout controlado  
5. Rollback automático si falla  
6. Notificación al equipo  

---

