# Comparativa: Patrón Factory vs Patrón Prototype

## Introducción
Los patrones **Factory** y **Prototype** pertenecen a la categoría de *creación de objetos* dentro del diseño orientado a objetos. Ambos resuelven el problema de **cómo generar instancias de manera flexible y desacoplada**, pero sus enfoques son distintos.

## Patrón Factory
El patrón **Factory Method** encapsula la lógica de creación dentro de una clase “fábrica”, delegando a subclases o funciones específicas la responsabilidad de decidir qué tipo de objeto instanciar.  
En este patrón, el foco está en **ocultar los detalles de construcción** y **promover la extensibilidad**, de forma que se pueda añadir un nuevo tipo de recurso sin modificar código existente.  
En la práctica, resulta útil cuando los objetos creados requieren configuración inicial o dependen de condiciones externas (por ejemplo, `NullResourceFactory` o `TimestampedNullResourceFactory` en Terraform simulado).

## Patrón Prototype
El patrón **Prototype**, en cambio, crea nuevos objetos **mediante la clonación de un objeto base o prototipo**.  
Su ventaja radica en que permite crear copias de estructuras complejas sin depender de constructores o inicializaciones costosas.  
En la infraestructura simulada, este patrón se usa para generar módulos o recursos derivados de una plantilla (`ResourcePrototype`), garantizando consistencia y eficiencia.

## Comparativa
| Aspecto | Factory | Prototype |
|----------|----------|------------|
| Enfoque | Creación desde cero | Clonación de una base existente |
| Ventaja | Desacopla la lógica de construcción | Acelera la replicación de estructuras |
| Uso ideal | Objetos con lógica de inicialización variable | Objetos similares que cambian levemente |
| Ejemplo práctico | Generar recursos nulos o con timestamp | Duplicar módulos o configuraciones base |

## Conclusión
Factory y Prototype pueden coexistir. El primero controla **cómo se crean** los objetos, mientras que el segundo optimiza **cómo se replican**.  
En proyectos de infraestructura como código, combinarlos permite construir plantillas base (Prototype) y, a la vez, decidir su origen dinámico o tipo (Factory), logrando una arquitectura modular, extensible y escalable.
