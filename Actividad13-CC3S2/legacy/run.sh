#!/bin/bash
# Script legacy de ejemplo
# Lee config.cfg por simplicidad en este demo
source "$(dirname "$0")/config.cfg"
echo "Arrancando ${NAME} en puerto ${PORT} en la red ${NETWORK}"