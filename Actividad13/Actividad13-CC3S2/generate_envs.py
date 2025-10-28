#!/usr/bin/env python3
"""
generate_envs.py
- Genera carpetas de environments (app1, app2, env3) a partir de la plantilla en modules/simulated_app/.
- Lee API_KEY desde la variable de entorno API_KEY o desde ~/.config/secure.json
- Opcional: interfaz CLI con click (--count, --prefix, --port)
- Valida JSON producido con jq si está disponible.
"""
import os
import json
import shutil
from pathlib import Path

try:
    import click
except Exception:
    click = None

ROOT = Path(__file__).parent
MODULE_DIR = ROOT / "modules" / "simulated_app"
ENV_DIR = ROOT / "environments"

DEFAULTS = [
    {"dir": "app1", "name": "app1", "network": "lab-net", "port": 8080},
    {"dir": "app2", "name": "app2", "network": "net2", "port": 8081},
    {"dir": "env3", "name": "env3", "network": "net2-peered", "port": 8082}
]

SECURE_PATH = Path(os.path.expanduser("~")) / ".config" / "secure.json"

def read_secure_api_key():
    # Primero desde env
    api_key = os.environ.get("API_KEY")
    if api_key:
        return api_key
    # Luego desde ~/.config/secure.json si existe
    if SECURE_PATH.exists():
        try:
            data = json.loads(SECURE_PATH.read_text(encoding="utf-8"))
            return data.get("api_key")
        except Exception:
            return None
    return None

def load_module_templates():
    tpl_network = {}
    tpl_main = {}
    net_file = MODULE_DIR / "network.tf.json"
    main_file = MODULE_DIR / "main.tf.json"
    if net_file.exists():
        tpl_network = json.loads(net_file.read_text(encoding="utf-8"))
    if main_file.exists():
        tpl_main = json.loads(main_file.read_text(encoding="utf-8"))
    return tpl_network, tpl_main

def write_json_checked(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")
    # Si jq está disponible, formatea/valida (silencioso si falla)
    if shutil.which("jq"):
        try:
            os.system(f"jq . {path} > {path}.tmp && mv {path}.tmp {path}")
        except Exception:
            pass

def generate_envs(specs):
    tpl_network, tpl_main = load_module_templates()
    api_key = read_secure_api_key()
    for s in specs:
        env_path = ENV_DIR / s["dir"]
        env_path.mkdir(parents=True, exist_ok=True)
        # Crear network.tf.json para el entorno: sobrescribe defaults
        net_vars = {
            "variable": {
                "network": {
                    "type": "string",
                    "default": s["network"],
                    "description": f"Red para {s['name']}"
                },
                "name": {
                    "type": "string",
                    "default": s["name"],
                    "description": "Nombre de la instancia"
                },
                "port": {
                    "type": "number",
                    "default": s["port"],
                    "description": "Puerto de la app"
                },
                "api_key": {
                    "type": "string",
                    "default": "" if not api_key else api_key,
                    "description": "API key (no versionada)"
                }
            }
        }
        write_json_checked(env_path / "network.tf.json", net_vars)

        # Crear main.tf.json (copiando estructura del módulo, pero con triggers que usan variables)
        main = {
            "resource": {
                "null_resource": {
                    "local_server": {
                        "triggers": {
                            "name": "${var.name}",
                            "network": "${var.network}",
                            "port": "${var.port}"
                        },
                        "provisioner": [
                            {
                                "local-exec": {
                                    "command": "echo 'Starting ${var.name} on port ${var.port} in network ${var.network}'"
                                }
                            }
                        ]
                    }
                }
            }
        }
        write_json_checked(env_path / "main.tf.json", main)
    print(f"Generated {len(specs)} environment(s) in {ENV_DIR}")

@click.command()
@click.option("--count", default=3, help="Número de entornos a generar (usa los primeros si se especifica)")
@click.option("--prefix", default="", help="Prefijo para nombres (ej: staging-). Si se pasa, reemplaza los nombres por prefixN")
@click.option("--start-port", default=None, type=int, help="Puerto inicial; si se pasa, asigna puertos consecutivos")
def cli(count, prefix, start_port):
    specs = DEFAULTS.copy()
    if count and count < len(specs):
        specs = specs[:count]
    if prefix:
        for i, s in enumerate(specs, start=1):
            s["name"] = f"{prefix}{i}"
            s["dir"] = s["name"]
    if start_port:
        for i, s in enumerate(specs):
            s["port"] = start_port + i
    generate_envs(specs)

if __name__ == "__main__":
    if click:
        cli()
    else:
        # modo sin click
        generate_envs(DEFAULTS)