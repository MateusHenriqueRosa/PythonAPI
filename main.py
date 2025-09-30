from clients.callmebot_service import CallMeBotService
from clients.conversor_service import CoinConversorService

import os

if __name__ == "__main__":
    arquivo_configuracao = os.path.join(os.getcwd(), "settings.json")

    client = CoinConversorService()
    conversao = client.converter("BTC", "BRL")

    wpp_service = CallMeBotService(arquivo_configuracao)
    texto,status = wpp_service.send_image(message=f"Valor do BTC: R${conversao}")
