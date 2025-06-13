import os

print("[+] Vérification des flags...")
flags = {
    "dvwa": "ER{dvwa_web_shell_access}",
    "ftp": "ER{ftp_file_exfiltration}",
    "ssh": "ER{ssh_weak_password_found}"
}

found = 0
for service, expected in flags.items():
    try:
        with open(f"../flags/{service}/flag.txt") as f:
            content = f.read().strip()
            if content == expected:
                print(f"[✔] {service} : flag correct")
                found += 1
            else:
                print(f"[✘] {service} : flag incorrect")
    except FileNotFoundError:
        print(f"[!] {service} : flag manquant")

print(f"\nTotal : {found}/{len(flags)} flags trouvés")
