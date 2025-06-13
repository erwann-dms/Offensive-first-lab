#!/bin/bash
echo "[*] Lancement du lab de pentest..."
docker-compose up -d --build
echo "[+] Lab démarré. Accédez à DVWA via http://localhost:8081"
