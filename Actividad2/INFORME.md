# Actividad 2: HTTP, DNS, TLS y 12-Factor

## Evidencias y Respuestas

### 1) HTTP: Fundamentos y herramientas
- Evidencia de ejecución de la app:
  
 ```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.22.75.112:8080
  ```
- Resultados de los comandos `curl`:

```
Pruebas en una terminal:


```
 [Request received - message: Hola CC3S2, release: v1
 127.0.0.1 - - [12/Sep/2025 16:48:12] "GET / HTTP/1.1" 200 -]

 [127.0.0.1 - - [12/Sep/2025 16:49:25] "POST / HTTP/1.1" 200 -]
 ```


- Resultado del comando `ss`:
  ```
  LISTEN 0      128           0.0.0.0:8080       0.0.0.0:*    users:(("python3",pid=6517,fd=3))
  ```

- Explicación: ¿Qué pasa si cambias MESSAGE o RELEASE sin reiniciar el proceso?
Si cambias las variables de entorno `MESSAGE`
Si cambias las variables de entorno MESSAGEo RELEASE sin reiniciar el proceso , la aplicación Flask no va a reflejar el cambio en la respuesta. Esto se debe a que, cuando se inicia la aplicación, las variables de entorno ( os.getenv("MESSAGE")y os.getenv("RELEASE")) se leen una sola vez , y sus valores quedan fijos en la memoria del proceso de Python.


### 2) DNS: nombres, registros y caché
- Hosts local:

  ```
  127.0.0.1 miapp.local
  ```
- Resultado de dig y getent:
  ```
  [PING miapp.local (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.073 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.057 ms



- Explicación de TTL/caché:

  
  ```
es un valor numérico que determina el tiempo que un servidor de caché DNS puede servir un registro DNS antes de alcanzar el servidor DNS autorizado y conseguir una nueva copia del registro.
  ```


- Diferencia entre /etc/hosts y zona DNS autoritativa:


  ```
   /etc/hosts es un archivo local en un solo sistema que contiene mapeos directos de nombres a direcciones IP, mientras que la zona DNS autoritativa es una colección global de registros de un dominio gestionada por un servidor de nombres, que responde a consultas de cualquier otro sistema en Internet.
  ```

### 3) TLS: seguridad en tránsito con Nginx como reverse proxy
- Comando y evidencia de certificado:
  ```
  (venv) bianca007@MSI:/mnt/c/Users/Bianca/Documents/Actividad2-CC3S2$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout miapp.key -out miapp.crt \
  -subj "/CN=miapp.local"
.......+......+.+..+.+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+..+.+........+....+..+....+.....+......+.+..+..........+.....+...+...+....+...........+.+........+.+......+......+...+......+...+..+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...........+..+.+..+......+.......+....

  ```


