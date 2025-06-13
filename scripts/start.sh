#!/bin/bash
echo "[*] Démarrage du lab Offensive..."
docker-compose pull
docker-compose build
docker-compose up -d

echo "[*] Lab démarré. Accès via http://localhost/"
