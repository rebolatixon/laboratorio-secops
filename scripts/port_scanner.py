import socket
import argparse
from datetime import datetime


def scan_port(host, port):
    """Tenta ligar-se a uma porta e devolve True se estiver aberta"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def main():
    parser = argparse.ArgumentParser(description="Port scanner simples")
    parser.add_argument("host", help="IP ou domínio do alvo")
    parser.add_argument("-p", "--ports", default="22,80,443,3000,4000",
                        help="Portas a verificar (separadas por vírgula)")
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",")]


    print(f"\n A scanear {args.host}")
    print(f" Inicio: {datetime.now()}")
    print("-" * 40)


    for port in ports:
        if scan_port(args.host, port):
            print(f"Porta {port} - ABERTA")

        else:

            print(f"Porta {port} - FECHADA")


    print("-" * 40)
    print(f" Fim: {datetime.now()}")

if __name__ == "__main__":
    main()

