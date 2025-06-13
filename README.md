# Offensive first Lab

**Offensive Lab** est un environnement clé-en-main de **pentest local**, conçu avec Docker Compose. Il regroupe plusieurs services vulnérables dans un réseau isolé pour s'exercer à des attaques de cybersécurité offensive.

---

## Services inclus

| Service    | Description                                        | Port local             |
|------------|----------------------------------------------------|------------------------|
| DVWA       | Application web vulnérable (XSS, SQLi, etc.)       | `http://localhost:8081` |
| FTP        | Serveur FTP avec accès anonyme                     | `localhost:21`         |
| SSH        | Serveur SSH avec mot de passe faible               | `localhost:2222`       |
| WordPress  | CMS vulnérable                                     | `http://localhost:8082` |
| WebDAV     | Stockage WebDAV avec authentification faible       | `http://localhost:8083` |
| Attacker   | Kali Linux prêt à l’emploi pour attaquer le lab    | shell CLI              |
| Proxy      | Nginx reverse proxy (accès aux services web)       | `http://localhost/`    |
| Scoring    | Serveur Flask de soumission de flag                | `http://localhost:5000` |
| WordPress  | CMS vulnérable                                     | `http://localhost:8082` |
| WebDAV     | Serveur WebDAV (upload vulnérable)                 | `http://localhost:8083` |
| Kali       | Conteneur d’attaque (outils installés)             | `accès via Docker CLI` |

---

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Système compatible Linux, macOS ou WSL (Windows)

---

## Installation & Lancement

```bash
git clone https://github.com/votre-utilisateur/offensive-lab.git
cd offensive-lab
cp .env.example .env
chmod +x scripts/start.sh
./scripts/start.sh
```

---

## Reset

Pour réinitialiser totalement le lab (conteneurs + volumes) :

```bash
./scripts/reset.sh
```

---

## Accès aux services

| Service    | URL / Port                |
|------------|---------------------------|
| DVWA       | `http://localhost:8081`   |
| FTP        | `ftp://localhost:21`      |
| SSH        | `ssh root@localhost -p 2222` |
| WordPress  | `http://localhost:8082`   |
| WebDAV     | `http://localhost:8083`   |
| Proxy      | `http://localhost/`       |
| Kali (CLI) | `docker exec -it kali bash` |

Identifiants par défaut disponibles dans `.env.example` si fournis.

---

## Exemple d’attaque guidée : DVWA

### Objectif : Obtenir un shell sur DVWA

#### Scan initial
```bash
nmap -sV -p- localhost
```

#### Accès à DVWA
URL : http://localhost:8081  
Identifiants par défaut : admin / password

#### Configurer DVWA
Dans « DVWA Security » → mettre sur « Low »

#### Injection SQL
Menu « SQL Injection »  
Tester : `1' OR '1'='1`

#### Obtenir un shell (optionnel)
Uploader un PHP reverse shell  
Accéder via l’URL du fichier uploadé  
Récupérer `flag.txt`

---

## Extensions incluses

- Brute-force SSH via hydra
- Lecture de fichiers sensibles via FTP anonyme
- Uploads WebDAV et récupération de fichiers
- WordPress vulnérable (ex: plugins ou login bruteforce)
- Kali Linux intégré pour lancer les attaques
- Scoring script pour valider les flags récupérés
- Guides & Cheatsheets dans `docs/`

---

## Système de scoring (Dashboard)

Interface web : http://localhost:5000

Soumission via submit_flag.py

---

## Soumission de flag

Un script client (submit_flag.py) est fourni. Exemple d’utilisation :

```bash
python3 submit_flag.py le_service le_flag
```
Le serveur retourne si le flag est valide.

---

## Avertissement

⚠️ Ce lab est uniquement à usage pédagogique. Ne jamais l’exposer sur Internet ni l’utiliser sur une infrastructure réelle sans autorisation.

---

## Arborescence du projet

```bash
offensive-first-lab/
├── attacker/
│   └── kali/
│       └── Dockerfile
├── flags/
│   ├── dvwa/flag.txt
│   ├── ftp/flag.txt
│   └── ssh/flag.txt
├── proxy/
│   ├── Dockerfile
│   └── nginx.conf
├── scoring/
│   └── scoring-server.py
├── scripts/
│   ├── reset.sh
│   └── start.sh
├── services/
│   ├── dvwa/Dockerfile
│   ├── ftp/Dockerfile
│   ├── ssh/Dockerfile
│   └── webdav/
│       ├── Dockerfile
│       └── webdav.conf
├── submit_flag.py
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## Bonus

- ✅ Reverse proxy intégré (NGINX)
- ✅ Réseau Docker dédié pour l’isolation
- ✅ Container Kali Linux intégré
- ✅ Scripts de scoring & validation des flags

---

## LICENSE

MIT
