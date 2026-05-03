#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${HOME}/.kimi/skills"

echo "Installing camk skill pack to ${SKILLS_DIR}..."

mkdir -p "${SKILLS_DIR}"

# Remove old camk/ folder if exists (from previous install)
if [ -d "${SKILLS_DIR}/camk" ]; then
    echo "  Removing old: camk"
    rm -rf "${SKILLS_DIR}/camk"
fi

# Auto-discover and install every skill folder under camk/
for skill_path in "${SCRIPT_DIR}/camk"/*/; do
    skill=$(basename "${skill_path}")
    if [ -d "${SKILLS_DIR}/${skill}" ]; then
        echo "  Replacing: ${skill}"
        rm -rf "${SKILLS_DIR}/${skill}"
    else
        echo "  Installing: ${skill}"
    fi
    cp -r "${skill_path}" "${SKILLS_DIR}/"
done

echo "Done. Skills installed:"
if ls -d ${SKILLS_DIR}/*/ >/dev/null 2>&1; then
    ls -d ${SKILLS_DIR}/*/ | xargs -n1 basename | sort
else
    echo "  (none)"
fi
