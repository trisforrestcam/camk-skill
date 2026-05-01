#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${HOME}/.kimi/skills"

echo "Installing camk skills to ${SKILLS_DIR}..."

mkdir -p "${SKILLS_DIR}"

for skill in docs dev debug brainstorm git-push; do
    if [ -d "${SCRIPT_DIR}/camk/${skill}" ]; then
        if [ -d "${SKILLS_DIR}/${skill}" ]; then
            echo "  Replacing: camk:${skill}"
            rm -rf "${SKILLS_DIR}/${skill}"
        else
            echo "  Installing: camk:${skill}"
        fi
        cp -r "${SCRIPT_DIR}/camk/${skill}" "${SKILLS_DIR}/"
    fi
done

echo "Done. Skills installed:"
ls -d ${SKILLS_DIR}/*/ 2>/dev/null | xargs -n1 basename | sort
