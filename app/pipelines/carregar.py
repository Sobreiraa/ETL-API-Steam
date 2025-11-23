import pandas as pd
import os

def carregar_dados_csv(jogos, caminho_pasta, nome_arquivo):
    # Garante que a pasta existe
    os.makedirs(caminho_pasta, exist_ok=True)

    # Normaliza os dados: transforma listas/dicts internos em string
    for jogo in jogos:
        for key, value in jogo.items():
            if isinstance(value, (list, dict)):
                jogo[key] = str(value)

    # Cria DataFrame único
    df = pd.DataFrame(jogos)

    # Caminho completo do arquivo
    arquivo_path = os.path.join(caminho_pasta, f"{nome_arquivo}.csv")

    # Salva CSV
    df.to_csv(arquivo_path, index=False, encoding='utf-8-sig')

    print(f"Arquivo salvo com sucesso em: {arquivo_path}")
    return arquivo_path

