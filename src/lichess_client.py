# Importamos a biblioteca 'requests', que permite fazer requisições HTTP.
# Sem ela, seria muito mais trabalhoso enviar GET/POST manualmente.
import requests


def get_games(username, max_games=5):
    """
    Função que consulta partidas de um usuário no Lichess.
    Ela retorna uma lista de linhas NDJSON, onde cada linha representa uma partida.
    
    Parâmetros:
    - username: nome do usuário no Lichess
    - max_games: quantidade máxima de partidas a buscar
    """

    # Montamos a URL da API pública do Lichess.
    # A API segue o padrão: https://lichess.org/api/games/user/<username>
    url = f"https://lichess.org/api/games/user/{username}"

    # Parâmetros opcionais da API.
    # Aqui pedimos:
    # - max: número máximo de partidas
    # - pgnInJson: incluir informações da partida em formato JSON
    # - moves: False → não queremos a lista completa de lances (para simplificar)
    params = {
        "max": max_games,
        "pgnInJson": True,
        "moves": False
    }

    # Enviamos a requisição GET para o Lichess.
    # 'requests.get' retorna um objeto com status, cabeçalhos e conteúdo.
    response = requests.get(url, params=params)

    # Se o status não for 200 (OK), algo deu errado.
    # Pode ser usuário inexistente, limite da API, etc.
    if response.status_code != 200:
        print(f"Erro ao consultar Lichess: {response.status_code}")
        return None

    # A API retorna NDJSON (Newline Delimited JSON):
    # Cada linha é um JSON separado representando uma partida.
    # Por isso dividimos o texto em linhas.
    games = response.text.split("\n")

    # Retornamos a lista de partidas.
    return games

