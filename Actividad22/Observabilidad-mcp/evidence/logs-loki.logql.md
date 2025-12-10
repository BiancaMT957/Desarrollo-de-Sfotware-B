# Logs con Loki y LogQL

Se generaron logs desde la aplicación demo ejecutando peticiones a los endpoints:

- /api/v1/items
- /api/v1/work
- /api/v1/error
- /healthz

Se observaron los siguientes tipos de logs:

- INFO: Peticiones exitosas
- WARNING: Simulación de requests lentos
- ERROR: Errores 500 simulados

Estos logs fueron visualizados mediante el comando:

docker-compose logs --tail 20

Los logs permitirán ser consultados en Loki usando consultas LogQL para detectar errores y latencias.
