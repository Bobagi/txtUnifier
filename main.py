import os
import re


def unify_txt_files(source_dir, destination_dir, unified_filename):
    # Cria o diretório de destino se não existir
    os.makedirs(destination_dir, exist_ok=True)

    # Caminho completo para o arquivo unificado
    unified_path = os.path.join(destination_dir, unified_filename)

    # Lista todos os arquivos no diretório fonte
    files = os.listdir(source_dir)

    # Filtra apenas os arquivos TXT e ordena pela numeração
    txt_files = sorted(
        [file for file in files if file.endswith(".txt")],
        key=lambda x: int(re.search(r"\d+", x).group()),
    )

    # Abre o arquivo unificado em modo de escrita
    with open(unified_path, "w") as unified_file:
        # Processa cada arquivo TXT ordenadamente
        for txt_file in txt_files:
            txt_path = os.path.join(source_dir, txt_file)
            with open(txt_path, "r") as file:
                # Escreve o conteúdo no arquivo unificado
                unified_file.write(file.read())

    print(f"Todos os arquivos TXT foram unificados em {unified_path}")


# Diretório de origem e destino
source_directory = "files"
destination_directory = "result"
output_filename = "unified.txt"

# Chama a função para unificar os arquivos
unify_txt_files(source_directory, destination_directory, output_filename)
