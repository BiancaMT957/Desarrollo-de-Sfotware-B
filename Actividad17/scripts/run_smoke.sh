#!/usr/bin/env bash
set -euo pipefail

# run_smoke.sh
# Runs quick smoke checks for each module:
#  - terraform init -backend=false
#  - terraform fmt -check
#  - terraform validate
#  - terraform plan -refresh=false (out -> /tmp)

MODULES=(network compute storage firewall dns)
TIMEOUT_PER_MODULE=8  # seconds, tuned for local machine; adjust if needed

echo "Starting smoke tests for modules: ${MODULES[*]}"
start_all=$(date +%s)
passed=0
failed=0

for m in "${MODULES[@]}"; do
  echo "---- Module: $m ----"
  pushd "modules/$m" >/dev/null 2>&1 || { echo "Missing modules/$m"; failed=$((failed+1)); continue; }

  # init (no backend) quietly
  terraform init -backend=false -input=false >/dev/null 2>&1 || true

  # fmt
  if timeout ${TIMEOUT_PER_MODULE} terraform fmt -check -diff >/dev/null 2>&1; then
    echo "fmt: OK"
  else
    echo "fmt: FAILED (or changes needed)"
    failed=$((failed+1))
    popd >/dev/null 2>&1
    continue
  fi

  # validate
  if timeout ${TIMEOUT_PER_MODULE} terraform validate >/dev/null 2>&1; then
    echo "validate: OK"
  else
    echo "validate: FAILED"
    failed=$((failed+1))
    popd >/dev/null 2>&1
    continue
  fi

  # plan (refresh=false)
  PLAN_TMP="/tmp/plan_${m}.tfplan"
  if timeout ${TIMEOUT_PER_MODULE} terraform plan -input=false -refresh=false -out="${PLAN_TMP}" >/dev/null 2>&1; then
    echo "plan: OK"
    # extract a contractual key (example: rules_count or host_count)
    if terraform show -json "${PLAN_TMP}" >/dev/null 2>&1; then
      echo "plan show: OK"
    fi
    passed=$((passed+1))
  else
    echo "plan: FAILED"
    failed=$((failed+1))
  fi

  # cleanup
  rm -f "${PLAN_TMP}" >/dev/null 2>&1 || true
  popd >/dev/null 2>&1
done

end_all=$(date +%s)
total_time=$((end_all - start_all))

echo "Smoke tests completed in ${total_time}s — Passed: ${passed}, Failed: ${failed}"
exit $((failed > 0))