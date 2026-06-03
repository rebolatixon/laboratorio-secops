import re
from collections import Counter


# No Rocky Linux, os logs de autenticação estão em /var/log/secure
log_file = "/var/log/secure"


try:
    with open(log_file, "r") as f:
        logs = f.readlines()
except FileNotFoundError:
    print(f"Ficheiro {log_file} não encontrado. A usarlogs de exemplo.")
    logs = [
        "Apr 10 10:00:01 localhost sshd[1234]: Failed password for root from 192.168.56.105",
        "Apr 10 10:00:02 localhost sshd[1235]: Failed password for root from 192.168.56.105",
        "Apr 10 10:00:03 localhost sshd[1236]: Failed password for root from 192.168.56.105",
        "Apr 10 10:00:04 localhost sshd[1237]: Failed password for root from 192.168.56.106",
        "Apr 10 10:00:05 localhost sshd[1238]: Failed password for root from 192.168.56.106",
        "Apr 10 10:00:06 localhost sshd[1239]: Failed password for root from 192.168.56.107",
        "Apr 10 10:00:07 localhost sshd[1240]: Failed password for root from 192.168.56.107",
        "Apr 10 10:00:08 localhost sshd[1241]: Failed password for root from 192.168.56.107",
        "Apr 10 10:00:09 localhost sshd[1242]: Failed password for root from 192.168.56.107",
        "Apr 10 10:00:10 localhost sshd[1243]: Failed password for root from 192.168.56.107",
   ]


# Contar tentativas falhadas por IP
ip_contagem = Counter()


for line in logs:
    if "Failed password" in line:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            ip_contagem[ip] += 1

print("=" * 50)
print("IPs com mais de 5 tentativas falhadas:")
print("=" * 50)


for ip, count in ip_contagem.items():
    if count > 5:
        print(f"{ip} - {count} tentativas (ACIMA do limite)")
    else:
        print(f"{ip} - {count} tentativas (abaixo do limite)")
