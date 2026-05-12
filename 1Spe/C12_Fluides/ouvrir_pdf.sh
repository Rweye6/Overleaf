#!/bin/bash

FILE="$1"
BASENAME="${FILE%.*}"

if [[ ! -f "$FILE" ]]; then
    echo "Fichier introuvable"
    exit 1
fi

echo "Conversion PDF → ODT..."
soffice --headless --convert-to odt "$FILE"

echo "Conversion ODT → DOC..."
soffice --headless --convert-to doc "${BASENAME}.odt"

echo "Terminé : ${BASENAME}.doc"
