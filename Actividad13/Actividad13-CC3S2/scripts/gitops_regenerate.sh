#!/usr/bin/env bash
# Script simple para GitOps local: si modules/simulated_app cambia, regenerar environments
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
echo "Regenerating environments from modules/simulated_app..."
python3 generate_envs.py
echo "Done."