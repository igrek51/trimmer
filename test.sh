#!/bin/bash
set -euo pipefail

MODULE_NAME=trimmer
PYTHON_INTERPRETER="${PYTHON_INTERPRETER:-python3}"

${PYTHON_INTERPRETER} -m coverage run --source ${MODULE_NAME} -m pytest -vv --tb=short -ra $@
# show code coverage info
${PYTHON_INTERPRETER} -m coverage report -m
