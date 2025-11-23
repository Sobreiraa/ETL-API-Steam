import requests


def extraindo_dados_API(APP_ID):
    # URL dos detalhes e reviews dos jogos, respectivamente
    URL_DETAILS = f'https://store.steampowered.com/api/appdetails?appids={APP_ID}&cc=br&l=portuguese'
    URL_REVIEW = f'https://store.steampowered.com/appreviews/{APP_ID}?json=1&language=brazilian'

    # Fazendo uma requisição para pegar os dados dos detalhes/reviews dos jogos da URL e convertendo em json
    response_details = requests.get(URL_DETAILS, timeout=5)
    response_review = requests.get(URL_REVIEW, timeout=5)

    data_details = response_details.json()
    data_review = response_review.json()

    # Verificando se o status da requisição é 200
    if response_details.status_code == 200 and response_review.status_code == 200:    
        if data_details[str(APP_ID)]["success"]: # Pegando os dados apenas se o retorno for SUCCESS
            if data_details[str(APP_ID)]['data']['is_free'] == True: # Verificando se o jogo é grátis
                game_details = {
                    "type": data_details[str(APP_ID)]['data']["type"],
                    "name": data_details[str(APP_ID)]['data']["name"],
                    "is_free": data_details[str(APP_ID)]['data']["is_free"],
                    "short_description": data_details[str(APP_ID)]['data']['short_description'],
                    "supported_languages": data_details[str(APP_ID)]['data']['supported_languages'],
                    "developers": data_details[str(APP_ID)]['data']['developers'],
                    "publishers": data_details[str(APP_ID)]['data']['publishers'],
                    "platforms": data_details[str(APP_ID)]['data']['platforms'],
                    "genres": data_details[str(APP_ID)]['data']['genres'][1]['description'],
                    "release_date": data_details[str(APP_ID)]['data']['release_date']['date'],
                    "starting price": 0, # Informando valores visto que o jogo é grátis
                    "current price": 0, # Informando valores visto que o jogo é grátis
                    "currency": "BRL"    
                }
            else: # Pegando os dados do jogo quando não é grátis
                game_details = {
                    "type": data_details[str(APP_ID)]['data']["type"],
                    "name": data_details[str(APP_ID)]['data']["name"],
                    "is_free": data_details[str(APP_ID)]['data']["is_free"],
                    "short_description": data_details[str(APP_ID)]['data']['short_description'],
                    "supported_languages": data_details[str(APP_ID)]['data']['supported_languages'],
                    "developers": data_details[str(APP_ID)]['data']['developers'],
                    "publishers": data_details[str(APP_ID)]['data']['publishers'],
                    "platforms": data_details[str(APP_ID)]['data']['platforms'],
                    "genres": data_details[str(APP_ID)]['data']['genres'][1]['description'],
                    "release_date": data_details[str(APP_ID)]['data']['release_date']['date'],
                    "starting price": data_details[str(APP_ID)]['data']['price_overview']['initial'],
                    "current price": data_details[str(APP_ID)]['data']['price_overview']['final'],
                    "currency": data_details[str(APP_ID)]['data']['price_overview']['currency'], 
                }
            
            if data_review['success'] == 1: # Verificando se o retorno é 1 de SUCCESS
                if "query_summary" in data_review: # Verificando se o jogo tem algum review
                    game_review = {
                        "review_score": data_review['query_summary']['review_score'],
                        "review_score_desc": data_review['query_summary']['review_score_desc'],
                        "total_positive": data_review['query_summary']['total_positive'],
                        "total_negative": data_review['query_summary']['total_negative'],
                        "total_reviews": data_review['query_summary']['total_reviews'],
                    }
                else: # Buscando os dados quando o jogo não tem review
                    game_review = {
                        "review_score": 'Não aplicável', # Informando valores visto que o jogo é grátis
                        "review_score_desc": 'Não aplicável', # Informando valores visto que o jogo é grátis
                        "total_positive": 0, # Informando valores visto que o jogo é grátis
                        "total_negative": 0, # Informando valores visto que o jogo é grátis
                        "total_reviews": 0, # Informando valores visto que o jogo é grátis
                    }
            
            # Juntando os dois dicionários
            game = game_details.copy()
            game.update(game_review)

            return game

