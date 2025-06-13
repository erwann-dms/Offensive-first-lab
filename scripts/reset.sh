#!/bin/bash
echo "[*] Arrêt du lab..."
docker compose down -v

echo "[*] Suppression des volumes et conteneurs..."
docker system prune -af --volumes

echo "[*] Nettoyage terminé. Relancez avec : ./scripts/start.sh"
