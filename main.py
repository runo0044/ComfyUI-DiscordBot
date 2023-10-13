import os

import coloredlogs
import requests
from dotenv import load_dotenv

from discord_bot import discord_bot
import call_Comfy_API


def main():
    # import .env file
    load_dotenv(override=True)
    coloredlogs.install("DEBUG", fmt="%(asctime)s %(levelname)s     %(name)s %(message)s",
                        field_styles={'asctime': {'color': 'green'}, 'levelname': {'color': 'blue', 'bold': True},
                                      'name': {'color': 'magenta'}, 'programname': {'color': 'cyan'}},
                        level_styles={'asctime': {'color': 'green'}, 'levelname': {'color': 'magenta', 'bold': True},
                                      'name': {'color': 'blue'}, 'programname': {'color': 'cyan'},
                                      'debug': {'color': 'blue', 'bold': True},
                                      'info': {'color': 'white', 'bold': True},
                                      'warning': {'color': 'yellow', 'bold': True},
                                      'error': {'color': 'red', 'bold': True},
                                      'critical': {'color': 'red', 'bold': True}})
    discord_bot()


if __name__ == "__main__":
    url = 'http://localhost:8188'
    api_list = ["/extensions", "/embeddings", "/queue", "/system_stats"]
    #for i in api_list:
    #    response = requests.get(url + i)
    #    print(i + "\n" + response.text)
    call_Comfy_API.txt2img("", "", 20, 8.0)
    # main()
