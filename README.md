# Offensive Lab

**Offensive Lab** est un environnement clé-en-main de **pentest local**, conçu avec Docker Compose. Il regroupe plusieurs services vulnérables dans un réseau isolé pour s'exercer à des attaques de cybersécurité offensive.

---

## Services inclus

| Service   | Description                                  | Port local     |
|-----------|----------------------------------------------|----------------|
| DVWA      | Application web vulnérable (XSS, SQLi, etc.) | `http://localhost:8081` |
| FTP       | Serveur FTP avec accès anonyme               | `localhost:21` |
| SSH       | Serveur SSH avec mot de passe faible         | `localhost:2222` |
| Proxy     | Nginx reverse proxy                          | `http://localhost/` |

---

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Système compatible Linux, macOS ou WSL (Windows)

---

## 🚀 Installation & Lancement

```bash
git clone https://github.com/votre-utilisateur/offensive-lab.git
cd offensive-lab
cp .env.example .env
chmod +x scripts/start.sh
./scripts/start.sh
```

---

## Accès aux services

| Service   | URL / Port    |
|-----------|----------------|
| DVWA      | `http://localhost:8081` |
| FTP       | `ftp://localhost:21` |
| SSH       | `ssh root@localhost -p 2222` |
| Proxy     | `http://localhost/` |

---

## Exemple d’attaque guidée
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

Tester : 1' OR '1'='1

#### Obtenir un shell (optionnel)

Uploader un PHP reverse shell

Accéder via l’URL du fichier uploadé

#### Extensions possibles:

- Brute-force SSH via hydra
- Lecture de fichiers sensibles via FTP anonyme
- Capture réseau (ex : tcpdump dans un container)
- Analyse de logs via un SIEM ajouté

---

## Avertissement

⚠️ Ce lab est uniquement à usage pédagogique. Ne jamais l’exposer sur Internet ni l’utiliser sur une infrastructure réelle sans autorisation.

---

## Arborescence du projet

```bash
offensive-lab/
├── docker-compose.yml
├── .env.example
├── scripts/
│   └── start.sh
├── services/
│   ├── dvwa/
│   │   └── Dockerfile
│   ├── ftp/
│   │   └── Dockerfile
│   └── ssh/
│       └── Dockerfile
├── proxy/
│   ├── Dockerfile
│   └── nginx.conf
└── README.md
```
---

## Bonus

Reverse proxy intégré (NGINX)

---

## Réseau Docker dédié pour l’isolation

Configuration centralisée via .env

---

## LICENSE

MIT
