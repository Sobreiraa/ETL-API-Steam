from app.pipelines.extrair import extraindo_dados_API
from bs4 import BeautifulSoup


def transformacao_dados(game_dataset):
    # Transformando o valor único do campo supported_languages em uma lista
    lista_original = game_dataset['supported_languages'].split(',')
    lista_linguas = []

    # Percorrendo cada item da lista original
    for n in lista_original:
        # Criando o objeto BeautifulSoup para remover HTML
        soup = BeautifulSoup(n, "html.parser")
        texto_limpo = soup.get_text()  # Remove todas as tags HTML

        # Limpando espaços no início/fim e tirando o texto de suport para áudio
        texto_limpo = texto_limpo.split('*')[0].strip() # Dividindo a string em 2 e pegando a parte correta

        # Adicionando na lista final
        lista_linguas.append(texto_limpo)

    game_dataset['supported_languages'] = lista_linguas # Inserindo a lista de vários valores

    # Platforms
    plataformas = game_dataset['platforms']
    plataformas_suportadas = [] # Variável para guardar os valores corretos

    # Iterando sobre chave/valor e pegando os valores que retornam True
    for chave, valor in plataformas.items():
        if valor:
            plataformas_suportadas.append(chave) # Adicionando as plataformas suportadas na variável
    
    game_dataset['platforms'] = plataformas_suportadas # Adicionando os valores corretos no dict

    return game_dataset # Retornando o dict 
