# Análisis de Escalabilidad

## Introducción
El experimento consistió en generar archivos JSON que representan configuraciones de infraestructura con 15 y 150 recursos, utilizando `MockBucketAdapter`.

## Resultados
El tamaño del archivo pasó de **5.4 KB** a **51.8 KB**, lo cual refleja un incremento aproximadamente lineal (≈9.6 veces).  
Esto sugiere que la estructura JSON no impone sobrecostos significativos en metadatos o serialización.

## Discusión
- **Escalabilidad lineal:** cada recurso incrementa el tamaño de manera proporcional.
- **Límite potencial:** en ejecuciones reales, la latencia de disco o red podría ser el factor limitante.
- **Mitigación:** se recomienda comprimir los archivos (`gzip`) o usar almacenamiento segmentado si se superan los 10 000 recursos.

## Conclusión
La arquitectura basada en patrones (Factory + Prototype + Adapter) escala de forma predecible, manteniendo la simplicidad del formato JSON sin penalizaciones graves de rendimiento.
