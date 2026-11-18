#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: ./scripts/init_conf.sh <NAZWA_KONFERENCJI> (np. ACL27)"
    exit 1
fi

CONF_NAME="$1"
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONF_DIR="$BASE_DIR/$CONF_NAME"

if [ -d "$CONF_DIR" ]; then
    echo "Dir $CONF_NAME exists ($CONF_DIR)."
    exit 1
fi

mkdir -p "$CONF_DIR/posters"
echo "[]" > "$CONF_DIR/processed.json"

echo "Created env for: $CONF_NAME"
echo "Upload photos to: $CONF_DIR/posters/"
