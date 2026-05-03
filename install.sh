#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${HOME}/.kimi/skills"

echo "Installing camk skill pack to ${SKILLS_DIR}..."

mkdir -p "${SKILLS_DIR}"

# Remove old camk/ and spec/ folders if exists (from previous install)
for old_pack in camk spec; do
    if [ -d "${SKILLS_DIR}/${old_pack}" ]; then
        echo "  Removing old: ${old_pack}"
        rm -rf "${SKILLS_DIR}/${old_pack}"
    fi
done

# Auto-discover and install every skill folder under camk/ and spec/
for pack_dir in "${SCRIPT_DIR}/camk" "${SCRIPT_DIR}/spec"; do
    for skill_path in "${pack_dir}"/*/; do
        skill=$(basename "${skill_path}")
        if [ -d "${SKILLS_DIR}/${skill}" ]; then
            echo "  Removing existing: ${skill}"
            rm -rf "${SKILLS_DIR}/${skill}"
        fi
        echo "  Installing: ${skill}"
        cp -r "${skill_path}" "${SKILLS_DIR}/"
    done
done

echo "Done. Skills installed:"
if ls -d ${SKILLS_DIR}/*/ >/dev/null 2>&1; then
    ls -d ${SKILLS_DIR}/*/ | xargs -n1 basename | sort
else
    echo "  (none)"
fi
