from app.pipelines.extrair import extraindo_dados_API
from app.pipelines.transformar import transformacao_dados
from app.pipelines.carregar import carregar_dados_csv
import pandas as pd

NUM_JOGOS_VALIDOS = 50
CSV_JOGOS = "data/input/steamcmd_appid.csv"
ID_INICIAL = 1010490

if __name__ == "__main__":
    df = pd.read_csv(CSV_JOGOS, header=None, names=["id", "name"])

    # Começar pelo ID desejado
    df = df[df["id"] >= ID_INICIAL]

    lista_ids = df["id"].tolist()

    todos_os_jogos = []
    tentativas = 0

    for app_id in lista_ids:
        if len(todos_os_jogos) >= NUM_JOGOS_VALIDOS:
            break

        tentativas += 1
        print(f"[Tentativa {tentativas}] Processando ID {app_id}...")

        try:
            game_dataset = extraindo_dados_API(app_id)
            game_dataset_tratado = transformacao_dados(game_dataset)

            todos_os_jogos.append(game_dataset_tratado)

            print(f"Jogo {app_id} processado com sucesso! Total: {len(todos_os_jogos)}")

        except Exception as e:
            print(f"Erro ao processar o ID {app_id}: {e}")

    caminho = carregar_dados_csv(todos_os_jogos, "data/output", "API_STEAM_GAMES_TODOS")
    print(f"Todos os jogos processados. Arquivo salvo em: {caminho}")
