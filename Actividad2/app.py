import os
from flask import Flask, jsonify
import logging
import sys

app = Flask(__name__)

# Configuración para logs a stdout (12-Factor)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

PORT = int(os.environ.get("PORT", 8080))
MESSAGE = os.environ.get("MESSAGE", "Hola CC3S2")
RELEASE = os.environ.get("RELEASE", "v1")

@app.route("/", methods=["GET"])
def home():
    log_msg = f"Request received - message: {MESSAGE}, release: {RELEASE}"
    app.logger.info(log_msg)
    return jsonify({
        "message": MESSAGE,
        "release": RELEASE
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)