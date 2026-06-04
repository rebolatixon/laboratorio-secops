import hashlib
import sys


def calcular_hash(ficheiro):
    sha256 = hashlib.sha256()
    try:
        with open(ficheiro, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 verificador_integridade.py <ficheiro>")
        sys.exit(1)
    ficheiro = sys.argv[1]
    hash_atual = calcular_hash(ficheiro)


    if hash_atual is None:
        print(f"Erro: Ficheiro '{ficheiro}' não encontrado.")
        sys.exit(1)


    print(f"Hash SHA256 de {ficheiro}: {hash_atual}")


    baseline_file = f"{ficheiro}.sha256"
    try:
        with open(baseline_file, "r") as f:
            hash_anterior = f.read().strip()


        if hash_atual == hash_anterior:
            print("   Ficheiro não foi alterado.")
        else:
            print("   Ficheiro foi alterado!")
    except FileNotFoundError:
        with open(baseline_file, "w") as f:
            f.write(hash_atual)
        print(f"Baseline guardado em {baseline_file}")


if __name__ == "__main__":
    main()
