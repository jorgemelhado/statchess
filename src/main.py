# Importamos a função get_games do módulo lichess_client.
# Isso separa responsabilidades: main.py usa a API, lichess_client.py conversa com ela.
from lichess_client import get_games


# Este bloco garante que o código só roda quando chamamos:
# python src/main.py
# (e não quando o arquivo é importado por outro módulo)
if __name__ == "__main__":

    # Definimos o usuário que queremos consultar.
    # Você pode trocar para qualquer usuário do Lichess.
    username = "BaldwinMyatt"

    # Chamamos a função que consulta a API.
    # Aqui pedimos apenas 3 partidas para simplificar.
    games = get_games(username, max_games=3)

    # Se a função retornou None, houve erro na API.
    if not games:
        print("Nenhuma partida encontrada ou erro na API.")
    else:
        print(f"Partidas encontradas para {username}:")

        # Percorremos cada linha retornada.
        # Cada linha é um JSON representando uma partida.
        for game in games:
            print("-" * 40)  # Apenas um separador visual
            print(game)      # Imprime o JSON bruto da partida

