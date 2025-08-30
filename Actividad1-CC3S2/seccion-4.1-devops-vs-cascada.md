# Sección 4.1 – DevOps vs Cascada

## Diagrama comparativo


El gráfico muestra que:
- **Cascada** sigue un flujo lineal de fases (Requisitos → Diseño → Implementación → Verificación → Mantenimiento), con retroalimentación tardía.  
- **DevOps** sigue ciclos iterativos con retroalimentación continua en cada etapa (Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → volver a Plan).

---

## Ventajas de DevOps
- **Automatización**: despliegues y pruebas automáticas reducen errores humanos.  
- **Lotes pequeños**: cambios frecuentes y de menor tamaño facilitan detectar problemas temprano.  
- **Feedback continuo**: retroalimentación inmediata de usuarios y del sistema, lo que acelera mejoras.  

---

## Caso donde cascada sí aplica
El modelo en cascada puede ser más adecuado cuando:
- Se desarrolla **software crítico en aviación**, donde cada fase debe estar completamente validada antes de pasar a la siguiente.  

---

## Criterios verificables
- **Certificaciones regulatorias** (ej: DO-178C en aviación, ISO 26262 en automoción).  
- **Dependencia fuerte de hardware**, donde cambios posteriores son muy costosos o inviables.  
