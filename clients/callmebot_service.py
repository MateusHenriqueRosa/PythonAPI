import requests
import json


class CallMeBotService:

    def __init__(self, arquivo_configuracao):
        self.__base_url = "https://api.callmebot.com/whatsapp.php"
        with open(arquivo_configuracao, "r") as arquivo:
            config = json.load(arquivo)
            self.__apikey = config.get("apikey")
            self.__telefone = config.get("telefone")

    def send_message(self, message):
        response = requests.get(
            url=f"{self.__base_url}?phone={self.__telefone}&text={message}&apikey={self.__apikey}"
        )
        return response.text, response.status_code
